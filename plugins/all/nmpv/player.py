
from __future__ import annotations

import time
import json
import socket

from typing import Optional, Any, Callable

import mpv  # type: ignore

from kwking_helper.config import c  # type: ignore
from kwking_helper.logging import CL  # type: ignore


DEFAULTS = c.dict('nmpv').get(socket.gethostname(), {})


class SyncError(Exception):
    def __init__(self, ts: float):
        super().__init__(float(ts))


class Player:
    MPV: mpv.MPV = None

    def __init__(self, ts: Optional[float] = None):
        self.__ts = ts
        self._custom = {
            'new': self.new,
            'quit': self.quit,
            'terminate': self.quit
        }

        self._logger = CL(
            c.main.get('plugin@nmpv', 'log_level'), name='MPV: Player',
            _file=c.main.get('plugin@nmpv', 'log_file', fallback=None)
        )

    @property
    def ts(self):
        return self.__ts

    @ts.setter
    def ts(self, value: Optional[float]):
        self.__ts = float(value) if value is not None else None

    @property
    def mpv(self):
        if Player.MPV is None:
            # @todo: add default flags
            self.new()

        return Player.MPV

    def __enter__(self):
        self.wait_for_sync()

        return self

    def __exit__(self, *args):
        pass

    def new(self, *flags, **kwargs):
        if isinstance(Player.MPV, mpv.MPV):
            self.logger('info', 'new', 'exit existing player instance')
            self.quit()

        Player.MPV = mpv.MPV(
            *flags,
            log_handler=self.logger,
            loglevel=c.main.get(
                'plugin@nmpv',
                'mpv_log_level',
                fallback=c.main.get('plugin@nmpv', 'log_level')
            ),
            **{**DEFAULTS, **kwargs}
        )

    def quit(self):
        if isinstance(Player.MPV, mpv.MPV):
            Player.MPV.quit(0)
            Player.MPV.terminate()
            del Player.MPV
            Player.MPV = None

    def wait_for_sync(self):
        if self.ts is None:
            return

        try:
            ts = self.ts - time.time()
            time.sleep(ts)
        except ValueError as ex:
            raise SyncError(ts) from ex

    def logger(self, level: str, component: str, message: str):
        if level in ['v', 'debug']:
            self._logger.debug(f"[{component}] {message}")

        elif level == 'info':
            self._logger.info(f"[{component}] {message}")

        elif level in ['warn', 'warning']:
            self._logger.warning(f"[{component}] {message}")

        elif level == 'error':
            self._logger.error(f"[{component}] {message}")

        elif level in ['fatal', 'critical']:
            self._logger.critical(f"[{component}] {message}")

        else:
            self._logger.warning(f"MPV LOGGER: unknown {level=}")

    def getattr(self, name: str):  # raises AttributeError if name not found in obj
        if name in self._custom:
            return self._custom[name]

        return getattr(self.mpv, name)

    def setattr(self, name: str, value: Any):
        setattr(self.mpv, name, value)

    def runattr(self, attr: Callable, *args, **kwargs):
        return attr(*args, **kwargs)
