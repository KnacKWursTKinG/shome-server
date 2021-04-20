#!/usr/bin/env python

import os
import pickle
import socket

from multiprocessing import Process
from typing import Optional, Union
from flask import Flask

import requests

from kwking_helper import rq, thread


class _Base:
    def __init__(self, host: str, port: int):
        self._host = socket.gethostbyname(host)
        self._port = int(port)

    def command(self, attr: str, *args, **kwargs):
        r = requests.post(
            f"http://{self._host}:{self._port}/api/nmpv/",
            data=pickle.dumps((str(attr), args, kwargs)),
            headers={
                'Content-Type': 'data/bytes'
            }
        )

        if r:
            return pickle.loads(r.content)

        raise rq.RQError(r)


class StreamRoute(_Base):
    def __init__(self, name: str, host: str = 'localhost', port: int = 50870):
        super().__init__(host, port)
        self.server = Flask(name)
        self.process = Process()

    def run(self, host: str = 'localhost', port: int = 0, debug: bool = False):
        if self.process.is_alive():
            return

        self.process = Process(
            target=self.server.run,
            args=(),
            kwargs=dict(host=host, port=port, debug=debug)
        )

    # TODO ...
    def start(self):
        """ generate port, start process, send play command """

    # TODO ...
    def new(self, filename):
        def stream():  # generator
            pass

        self.server.add_url_rule(
            ..., # route
            ..., # endpoint name
            stream  # func
        )


class Playlist(_Base):
    def __init__(self, host: str, port: int = 50870):
        super().__init__(host, port)
        self.__cache: list[dict[str, Union[str, int, bool]]] = list()
        self.refresh()

    def __iter__(self):
        self.__thread.join()

        for _ in self.__cache:
            yield _

    def __repr__(self):
        self.__thread.join()

        return f"{self.__cache!r}"

    def __str__(self):
        self.__thread.join()

        return '\n'.join(map(str, self.__cache))

    def refresh(self):
        """ load playlist """
        try:
            if self.__thread.is_alive():
                return
        except Exception:
            self.__thread = self.__refresh()

    @thread(True)
    def __refresh(self):
        self.__cache = self.command('playlist')

    def append(self, filename: str):
        """ append filename/url to playlist """
        self.command('playlist_append', filename)
        self.refresh()


class Player(_Base):
    def __init__(self, host: str, port: int = 50870, playlist: bool = True):
        super().__init__(host, port)
        self.__playlist: Optional[Playlist] = Playlist(host, port) if playlist else None

    def new(self, **player_args):
        self.command('new', **player_args)
        self.playlist.refresh()

    def play(self, filename: str):
        self.command('play', os.path.abspath(filename))
        self.playlist.refresh()

    # TODO: ...
    def stream(self, handler: StreamRoute):
        ...

    @property
    def playlist(self):
        return self.__playlist
