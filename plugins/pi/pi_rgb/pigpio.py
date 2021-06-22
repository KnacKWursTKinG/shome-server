""" pigpio server control """

import json
import os
import socket
import threading

from typing import Union

import pigpio

from helper.config import c
from helper.logging import CL
from helper.thread import threaded2  # @todo: ...


class Cache:
    thread_lock = threading.Lock()
    group = 'cache.pi_rgb'
    last_rgbw: dict[str, list[int]] = {}
    default_rgbw: list[int] = json.loads(c.main.get('plugin@pi_rgb', 'default'))

    logger = CL(
        c.main.get('plugin@pi_rgb', 'log_level'), "Pi_RGB: Cache",
        _file=os.path.expanduser(c.main.get('plugin@pi_rgb', 'log_file', fallback=None))
    )

    @classmethod
    def cache(cls, section: Union[str, int], rgbw: list[int]):
        cls.logger.debug(f"[cache] {section=}, {rgbw=}")

        if set(rgbw) == set([0]):
            return

        if cls.rgbw(section) != rgbw or not cls.last_rgbw.get(str(section)):
            cls.logger.debug(f"[cache] upload {rgbw=} to dbserver")
            r = c.db.post(
                '/label',
                data=json.dumps(rgbw),
                name=f"{socket.gethostname()}.{section}",
                group=cls.group
            )

            if not r:
                cls.logger.error(f"[cache] {r!r}, {r.text}")

        with cls.thread_lock:
            cls.last_rgbw[str(section)] = rgbw

    @classmethod
    def rgbw(cls, section: Union[str, int]) -> list[int]:
        cls.logger.debug(f"[rgbw] {section=}")

        if not cls.last_rgbw.get(str(section)):
            cls.logger.debug("[rgbw] download rgbw from dbserver")
            r = c.db.get('/label', name=f"{socket.gethostname()}.{section}", group=cls.group)

            if not r:
                cls.logger.error(f"[rgbw] {r!r}, {r.text}")
            else:
                rgbw = json.loads(r.text)

                if isinstance(rgbw, list):
                    cls.last_rgbw[str(section)] = rgbw

        with cls.thread_lock:
            return cls.last_rgbw.get(str(section), cls.default_rgbw)


class PigpioHandler(Cache):
    def __init__(self):
        super().__init__()

        self.log = CL(
            c.main.get('plugin@pi_rgb', 'log_level'), "Pi_RGB: PigpioHandler",
            _file=os.path.expanduser(c.main.get('plugin@pi_rgb', 'log_file', fallback=None))
        )

        self._range = c.main.getint('plugin@pi_rgb', 'range')
        # connect to pigpiod.service
        self.pi = None

        self.pi_init()
        self._set_range()

    def pi_init(self) -> pigpio:
        if self.pi:
            if self.pi.connected:
                return

            self.pi.stop()

        self.log.info("Connect to the pigpiod.service")
        del self.pi
        self.pi = pigpio.pi()

    @threaded2(daemon=False)
    def _set_range(self):
        for section, gpios in c.dict('pi_rgb').get(socket.gethostname(), {}).items():
            self.log.debug(f"set range for section '{section}' to {self._range}")
            self.log.debug(f"{section=}, {gpios=}")

            for gpio in json.loads(gpios):
                self.pi.set_PWM_range(int(gpio), self._range)

    @threaded2(daemon=False)
    def set_dutycycle(self, section: Union[str, int], rgbw: list[int]) -> None:
        self.log.debug(f"set rgbw ({rgbw=}) for {section=}")

        section = str(section)
        rgbw = revert_rgbw(rgbw, self._range)

        try:
            gpios = json.loads(c.pi_rgb.get(socket.gethostname(), section))

        except Exception as ex:
            self.log.critical(f"[section: {section}] Config Error: {ex}")
            raise ex

        for gpio, value in zip(gpios, rgbw):
            if int(gpio) == 0:
                continue

            self.pi.set_PWM_dutycycle(int(gpio), value)

        self.cache(section, revert_rgbw(rgbw, self._range))

    @threaded2(daemon=False)
    def get_dutycycle(self, section: Union[str, int]) -> list[int]:
        self.log.debug(f"get rgbw from {section=}")

        section = str(section)

        try:
            gpios = json.loads(c.pi_rgb.get(socket.gethostname(), section))
            self.log.debug(f"{gpios=}")

        except Exception as ex:
            self.log.critical(f"[section: {section}] Config Error: {ex}")
            raise ex

        try:
            rgbw = revert_rgbw([self.pi.get_PWM_dutycycle(int(g)) for g in gpios], self._range)

        except pigpio.error as ex:
            self.log.warning("[get_dutycycle] gpio pins not used yet")
            self.log.warning(f"[get_dutycycle] pigpio.error: {ex}")
            rgbw = [0, 0, 0, 0]

        return rgbw


def revert_rgbw(rgbw: list[int], _range: int) -> list[int]:
    return [_range - int(x) for x in rgbw]
