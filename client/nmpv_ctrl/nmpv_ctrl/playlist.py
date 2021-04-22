
import socket
import json
import pprint

from dataclasses import dataclass
from typing import Union, Optional

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
        return pprint.PrettyPrinter().pformat(self.__playlist)

    def __len__(self):
        return len(self.__playlist)

    def __contains__(self, item: Union[int, str, _PlaylistItem]):
        for _el in self.__playlist:
            if item in [_el.id, _el.filename, _el]:
                return True

        return False

    def __getitem__(self, index: int) -> _PlaylistItem:
        return self.__playlist[index]

    def __refresh__(self):
        self.logger.debug(f"reload playlist")

        self.__playlist = list()
        for _el in super().run('playlist'):
            self.__playlist.append(_PlaylistItem(**_el))

    def reload(self):
        self.__refresh__()

    def run(self, attr: str, *args, **kwargs):
        self.logger.debug(f"{attr=}, {args=}, {kwargs=}")
        _return = super().run(attr, *args, **kwargs)
        self.__refresh__()

        return _return

    def index(self, item: Union[int, _PlaylistItem]) -> int:
        for idx, _el in enumerate(self.__playlist):
            if item in [_el.id, _el]:
                return idx

        raise IndexError(item)

    @property
    def pos(self) -> int:
        return super().run('playlist_pos')

    @pos.setter
    def pos(self, pos: int):
        super().run('playlist_pos', int(pos))

    def append(self):
        """ @TODO: add file/url to playlist """

    def remove(self):
        """ @TODO: remove from playlist """

    def next(self):
        """ @TODO: play next in playlist """

    def prev(self):
        """ @TODO: play next in playlist """

    def shuffle(self):
        """ @TODO: shuffle playlist """

    def unshuffle(self):
        """ @TODO: unshuffle playlist """
