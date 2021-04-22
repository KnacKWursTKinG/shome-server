
import socket
import json
import pprint

from dataclasses import dataclass
from typing import Union

from nmpv_ctrl.ctrl import CTRL

from kwking_helper.logging import CL


__all__ = ['_PlaylistItem', 'Playlist']


@dataclass
class _PlaylistItem:
    filename: str
    id: int
    current: bool = False
    playing: bool = False


class Playlist(CTRL):
    def __init__(self, host: str, port: int = 50870, log_level: str = 'warning'):
        """ Playlist Handler

        Args:
            host: shomeserver hostname to control
            port: shomeserver port [default: 50870]

        Raises:
            socket.gaierror: if host not found
        """
        super().__init__(host, port)

        self.__playlist: list[_PlaylistItem] = list()
        self.logger = CL(
            log_level, f"{self!r}"
        )

    def __bool__(self):
        return bool(self.__playlist)

    def __repr__(self):
        return f"Playlist({self.host!r}, {self.port!r})"

    def __str__(self):
        return pprint.PrettyPrinter(indent=4).pformat(self.__playlist)

    def __len__(self):
        return len(self.__playlist)

    def __contains__(self, item):
        for _el in self.__playlist:
            if item in [_el.id, _el.filename]:
                return True

        return False

    def __getitem__(self, item):
        for _el in self.__playlist:
            if item in [_el.id, _el.filename]:
                return _el

        return None

    def __refresh__(self):
        self.logger.debug(f"reload playlist")

        self.__playlist = list()
        for _el in super().run('playlist'):
            self.__playlist.append(_PlaylistItem(**_el))

    def reload(self):
        self.__refresh__()
