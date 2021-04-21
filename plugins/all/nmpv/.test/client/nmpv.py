#!/usr/bin/env python

import os
import pickle
import socket
import mimetypes

from multiprocessing import Process
from typing import Optional, Union

import requests

from flask import Flask, Response

from kwking_helper import rq, thread


class Base:
    def __init__(self, host: str, port: int):
        self._host = socket.gethostbyname(host)
        self._port = int(port)

    def command(self, attr: str, *args, **kwargs):
        r = requests.post(
            f"http://{self._host}:{self._port}/api/nmpv/player",
            data=pickle.dumps((str(attr), args, kwargs)),
            headers={
                'Content-Type': 'data/bytes'
            }
        )

        if r:
            return pickle.loads(r.content)

        raise rq.RQError(r)


class Playlist(Base):
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


class Player(Base):
    def __init__(self, host: str, port: int = 50870, playlist: bool = True):
        super().__init__(host, port)
        self.__playlist: Optional[Playlist] = Playlist(host, port) if playlist else None

    def new(self, **player_args):
        self.command('new', **player_args)
        self.playlist.refresh()

    def play(self, file: str):
        self.command('play', file)
        self.playlist.refresh()

    def stream(self, file: str):
        stream = Stream(self._host, file)
        stream.start()
        self.play(stream.url)

    @property
    def playlist(self):
        return self.__playlist


class Stream(Process):
    Queue: set[Process] = set()

    def __init__(self, host: str, file: str):
        super().__init__()
        self.daemon = True

        self.file = os.path.expanduser(file)

        if not os.path.isfile(self.file):
            raise FileNotFoundError(self.file)

        self.mimetype = mimetypes.guess_type(self.file)[0]
        self.rule = f"/{id(self.file)}"
        self.endpoint = 'stream'

        self.port = 0
        self.host = host
        self.server = Flask(self.endpoint)

        self.gen_port()

        Stream.Queue.add(self)

    def __del__(self):
        Stream.Queue.remove(self)

    @property
    def url(self):
        return f"http://{self.host}:{self.port}{self.rule}"

    def run(self):
        def stream():
            def gen_from_file():
                with open(self.file, 'rb') as f:
                    while (data := f.read(1024*1024)):
                        yield data

            return Response(
                gen_from_file(), mimetype=self.mimetype
            )

        self.server.add_url_rule(
            rule=self.rule,
            endpoint=self.endpoint,
            view_func=stream
        )

        self.server.run(self.host, port=self.port)

    def gen_port(self):
        with socket.create_server(('localhost', 0)) as s:
            self.port = s.getsockname()[1]

        return self.port
