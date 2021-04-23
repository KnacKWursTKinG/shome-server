
import pprint

from dataclasses import dataclass
from typing import Union

from nmpvc.ctrl import Control

from kwking_helper.logging import CL

from nmpvc.stream import Stream


__all__ = ['_PlaylistItem', 'Playlist']


@dataclass
class _PlaylistItem:
    filename: str
    id: int
    current: bool = False
    playing: bool = False


class Playlist(Control):
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
        self.logger.debug("reload playlist")

        self.__playlist = list()
        for _el in super().run('playlist'):
            self.__playlist.append(_PlaylistItem(**_el))

    def reload(self):
        self.__refresh__()

    def index(self, item: Union[int, _PlaylistItem]) -> int:
        for idx, _el in enumerate(self.__playlist):
            if item in [_el.id, _el]:
                return idx

        raise IndexError(item)

    @property
    def pos(self) -> int:
        return self.run('playlist_pos')

    @pos.setter
    def pos(self, pos: int):
        self.run('playlist_pos', int(pos))

    def append(self, file: Union[str, Stream]):
        """ add file/url to playlist """
        if isinstance(file, Stream):
            _file = file.url
            file.start()
        else:
            _file = file

        return self.run('playlist_append', str(_file))

    def remove(self, index: Union[str, int] = 'current'):
        """ remove from playlist """
        return self.run('playlist_remove', index)

    def clear(self):
        """ Clear Playlist """
        return self.run('playlist_clear')

    def next(self, mode: str = 'weak'):
        """ play next in playlist """
        return self.run('playlist_next', mode)

    def prev(self, mode: str = 'weak'):
        """ play next in playlist """
        return self.run('playlist_prev', mode)

    def shuffle(self):
        """ shuffle playlist """
        return self.run('playlist_shuffle')

    def unshuffle(self):
        """ unshuffle playlist """
        return self.run('playlist_unshuffle')

    def play_index(self, index: int):
        """ Play index """
        return self.run('playlist_index', int(index))
