
import os
import pickle
import socket
import threading
import time

from dataclasses import dataclass, field

import requests

from kwking_helper import thread, c, ClickLogger, rq

from pirgb import config


class CacheError(Exception):
    pass


@dataclass
class _Section:
    label: str  # NOTE: strict format: "{host}:{section}"
    name: str  # NOTE: default should be the same as label
    groups: list[str] = field(default_factory=list)
    rgbw: list[tuple[int, ...]] = field(default_factory=list)
    last_change: float = time.time()


class Cache:
    thread_lock = threading.Lock()
    max_rgbw_cache: int = c.main.getint('pirgb', 'max_rgbw_cache')
    db_group = 'cache.pi_rgb'
    db_label = 'pirgb'
    _cache: dict[str, _Section] = dict()

    def __init__(self):
        self.cache_path = config.path[config.platform()]['cache'] + '/cache.pickle'
        self.logger = ClickLogger(c.main.get('pirgb', 'log_level'), 'Cache')

    @property
    def db(self):
        if not c.db:
            try:
                self.logger.info("[load] try reconnect to dbserver")
                c.db = rq.DBServer(
                    c.main.get('dbserver', 'credentials'),
                    c.main.get('dbserver', 'host'),
                    c.main.getint('dbserver', 'port')
                )

            except socket.error:
                self.logger.warning("[load] dbserver not reachable, using cache for now!")

        return c.db

    @property
    def cache(self) -> dict[str, _Section]:
        with Cache.thread_lock:
            return Cache._cache

    @thread(daemon=False, log_level=c.main.get('pirgb', 'log_level'))
    def load(self):
        # <<- loading data from dbserver and cache
        updated = False

        if c.main.getboolean('pirgb', 'use_cache') and os.path.isfile(self.cache_path):
            self.logger.debug(f"[load] load from cache {self.cache_path=!r}")
            updated = self.__cache_merge(pickle.load(open(self.cache_path, 'rb')))

        if c.main.getboolean('pirgb', 'use_db_config') and self.db:
            self.logger.debug(f"[load] load from dbserver {self.db.url=}")

            try:
                r = self.db.get(self.db_group, self.db_label)

                if r:
                    updated = self.__cache_merge(pickle.loads(r.content))
                else:
                    self.logger.warning(
                        f"[load] db: {r!r}, '{r.text}'"
                    )

                for host, data in c.dict('pi_rgb').items():
                    if host in ['DEFAULT', 'env']:
                        continue

                    for section in data:
                        _label = f"{host}:{section}"

                        if _label not in self.cache:
                            self.logger.debug(f"[load] {_label=} not in cache, create a new entry")
                            self.new(_label, groups=['ALL'])

            except requests.exceptions.ConnectionError:
                self.logger.error(
                    f"[load] dbserver ({self.db.url=}) not reachable!"
                )
                c.db = None

            except requests.exceptions.Timeout:
                self.logger.warning(f"[load] requests timout ({self.db.timeout=})")

        if updated:
            self.save()
        # ->>

    @thread(daemon=False, log_level=c.main.get('pirgb', 'log_level'))
    def save(self, skip_cache: bool = False):
        # <<- Save to db and cache
        if c.main.getboolean('pirgb', 'use_db_config') and self.db:
            self.logger.debug(f"[save] save cache to dbserver {self.db.url=}")

            try:
                r = self.db.put(
                    self.db_group, self.db_label,
                    data=pickle.dumps(self.cache),
                    _auto_post=True
                )

                if not r:
                    self.logger.error(
                        f"[save] Upload cache data to db failed: {r.text} [{r!r}]"
                    )

            except requests.exceptions.ConnectionError:
                self.logger.error(
                    f"[save] dbserver ({self.db.url=}) not reachable!"
                )
                c.db = None

            except requests.exceptions.Timeout:
                self.logger.warning("[save] requests timout")

        if c.main.getboolean('pirgb', 'use_cache') and self.cache and not skip_cache:
            self.logger.debug(f"[save] save cache to {self.cache_path=}")

            if not os.path.isdir(os.path.dirname(self.cache_path)):
                os.makedirs(os.path.dirname(self.cache_path))

            pickle.dump(
                self.cache,
                open(config.path[config.platform()]['cache'] + '/cache.pickle', 'wb')
            )
        # ->>

    def new(self, label: str, **defaults):
        if label in self.cache:
            raise CacheError(f"{label!r} exists in cache (use update)")

        self.cache[label] = _Section(label, label, **defaults, last_change=0)

    def update(self, label: str, append: bool = True, **kwargs):
        # <<- update existing label in cache
        self.logger.debug(f"[update] {label=!r}, {append=!r}, {kwargs=!r}")
        item = self.cache[label]

        # set kwargs
        for key, value in item.__dict__.items():
            if key == 'label':
                continue

            if isinstance(value, list) and key in kwargs:
                if not isinstance(kwargs[key], list):
                    raise CacheError(f"wrong type for {key!r}: {kwargs[key]!r}")

                if append:
                    self.logger.debug(f"[update] {key}: append {kwargs[key]=} to {value=}")
                    value.extend(kwargs[key])
                else:
                    self.logger.debug(f"[update] set new list for {key=}")
                    value = kwargs[key]

                self.logger.debug(f"[update] {value=}")
                #value = list(map(list, set(map(tuple, value))))
                value = list(set(value))

            elif isinstance(value, (int, float, str)) and key in kwargs:
                if not isinstance(kwargs[key], type(value)):
                    raise CacheError(f"wrong type for {key!r}: {kwargs[key]!r}")

                value = kwargs[key]

            else:
                self.logger.debug(f"[update] skip {key=!r}")
                continue

            item.__dict__[key] = value

        # set last_change
        item.last_change = time.time()

        self.cache[label] = item
        self.save()
        # ->>

    def __cache_merge(self, data: dict[str, _Section]) -> bool:
        # <<- set newest item to cache
        assert isinstance(data, dict),\
            f"[__cache_merge] data not from type '{dict!r}'"

        updated = False

        for _key, _data in data.items():
            assert isinstance(_data, _Section),\
                f"[__cache_merge] data value not from type '{_Section!r}'"

            if _key not in self.cache:
                self.cache[_key] = _data

                updated = True

            elif _data.last_change > self.cache[_key].last_change:
                self.cache[_key] = _data

                updated = True

        return updated
        # ->>
