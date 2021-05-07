""" Playlist handler (Main Client Class) """

from .mpv import MPVBase


__all__ = ['PL', 'Playlist']


class PL:
    def __init__(self, host: str, port: int = 50870):
        self.base = MPVBase(host, port)

    def next(self, mode='weak'):
        ...

    def prev(self, mode='weak'):
        ...

    def remove(self, index = 'current'):
        ...

    def append(self, url: str):
        ...

    def play(self, index):
        ...

    def suffle(self):
        ...

    def unsuffle(self):
        ...

    def clear(self):
        ...


Playlist = PL
