
from __future__ import annotations

import socket
import types
import json

from threading import Thread
from typing import Union, Optional, Any

import mpv

from kwking_helper.config import c
from kwking_helper.logging import CL


class Player(Thread):
    Queue: set[Player] = set()
    MPV: mpv.MPV = None

    try:
        PLAYER_ARGS = json.loads(
            c.mpv._sections.get(socket.gethostname(), '{}')
        )
    except AttributeError:
        PLAYER_ARGS = dict()

    def __init__(self, sync: Optional[float], attr, *args, **kwargs):
        super().__init__()
        self.daemon = True
        self.name = f"player-{id(self)}"

        self.mpv_attr = {
            'new': self.mpv_init,
            'quit': self.mpv_quit,
            'terminate': self.mpv_quit
        }
        self._mpv_attr_no_init = [
            'new',
            'quit',
            'terminate'
        ]

        self._sync = sync
        self._attr = attr
        self._args = args
        self._kwargs = kwargs

        self.logger = CL(
            c.main.get('plugin@nmpv', 'log_level'),
            name='MPV: Player',
            _file=c.main.get('plugin@nmpv', 'log_file', fallback=None)
        )

        self._error = None
        self._return = None

    def start(self):
        super().start()
        Player.Queue.add(self)

    def __del__(self):
        if self in Player.Queue:
            Player.Queue.remove(self)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.logger.debug(f"[__exit__] {args=}")
        self.__del__()

    def mpv_logger(self, level: str, component: str, message: str):
        if level in ['v', 'debug']:
            self.logger.debug(f"[{component}] {message}")

        elif level == 'info':
            self.logger.info(f"[{component}] {message}")

        elif level == 'warn':
            self.logger.warning(f"[{component}] {message}")

        elif level == 'error':
            self.logger.error(f"[{component}] {message}")

        elif level == 'fatal':
            self.logger.critical(f"[{component}] {message}")

        else:
            self.logger.warning(f"MPV LOGGER: unknown {level=}")

    def mpv_init(self, *extra_mpv_flags, **player_args):
        if isinstance(Player.MPV, mpv.MPV):
            self.logger.debug("quit existing player")
            _mpv = Player.MPV
            _mpv.quit(0)
            _mpv.terminate()
            del _mpv

        Player.MPV = mpv.MPV(
            *extra_mpv_flags,
            log_handler=self.mpv_logger, loglevel='debug',
            **player_args
        )

    def mpv_quit(self):
        if Player.MPV is not None:
            Player.MPV.quit(0)
            Player.MPV.terminate()
            del Player.MPV
            Player.MPV = None

    def run(self):
        self.logger.debug(f"[{self.name}] {self._attr=}, {self._args=}, {self._kwargs=}")

        if self._attr in self.mpv_attr:
            attr = self.mpv_attr[self._attr]

            if Player.MPV is None and self._attr not in self._mpv_attr_no_init:
                self.mpv_init()

        else:
            if Player.MPV is None:
                self.mpv_init()

            try:
                attr = getattr(Player.MPV, self._attr)

            except AttributeError as ex:
                self._error = ex
                self.logger.error(f"[{self.name}] {ex=}")
                return

        self.logger.debug(f"[{self.name}] got {attr=} (type: {type(attr)})")

        if isinstance(attr, types.MethodType):
            try:
                # @todo run on self._sync (timestamp) if set
                self._return = attr(*self._args, **self._kwargs)

            except Exception as ex:
                self._error = f"<{self._attr}(*{self._args}, **{self._kwargs})>, {ex.args[0]}"
                self.logger.error(f"[{self.name}] {self._error}")
                return

        else:
            if self._args:
                try:
                    # @todo run on self._sync (timestamp) if set
                    setattr(Player.MPV, self._attr, self._args[0])

                except Exception as ex:
                    self._error = f"<{self._attr} = ({self._args[0]})>, {ex.args[0]}"
                    self.logger.error(f"[{self.name}] {self._error}")
                    return
            else:
                # @todo run on self._sync (timestamp) if set
                self._return = attr
