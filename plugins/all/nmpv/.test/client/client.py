import os
import sys
import pickle
import time
import socket
import mimetypes

from multiprocessing import Process
from threading import Thread
from typing import Optional, Union

import requests

from flask import Flask, Response

from kwking_helper import rq
from kwking_helper.thread import thread


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
        self.thread.join()

        for _ in self.__cache:
            yield _

    def __repr__(self):
        self.thread.join()

        return f"{self.__cache!r}"

    def __str__(self):
        self.thread.join()

        return '\n'.join(map(str, self.__cache))

    def refresh(self):
        """ load playlist """
        try:
            if self.thread.is_alive():
                return
        except Exception:
            self.thread = self.__refresh()

    @thread(True)
    def __refresh(self):
        self.__cache = self.command('playlist')

    def append(self, file: str):
        """ append filename/url to playlist """
        self.command('playlist_append', file)
        self.refresh()


class Stream(Process):
    Queue: list[Process] = list()

    def __init__(self, host: str, file: str):
        super().__init__()
        self.daemon = True
        self.name = f"stream-{id(self)}"

        self.file = os.path.expanduser(file)

        if not os.path.isfile(self.file):
            raise FileNotFoundError(self.file)

        self.mimetype = mimetypes.guess_type(self.file)[0]
        self.rule = f"/{id(self.file)}"

        self.port = 0
        self.host = host
        self.server = Flask(self.name)

        self.gen_port()

    def start(self):
        super().start()
        Stream.Queue.append(self)

    def __del__(self):
        Stream.Queue.remove(self)

    @property
    def url(self):
        return f"http://{self.host}:{self.port}{self.rule}"

    def run(self):
        @self.server.after_request
        def quit(r):
            def _exit():
                time.sleep(1)
                os._exit(0)

            Thread(target=_exit).start()

            return r

        @self.server.route(self.rule)
        def stream():
            def gen_from_file():
                with open(self.file, 'rb') as f:
                    while (data := f.read(1024*1024)):
                        yield data

            return Response(
                gen_from_file(), mimetype=self.mimetype
            )

        self.server.run(self.host, port=self.port)

    def gen_port(self):
        with socket.create_server(('localhost', 0)) as s:
            self.port = s.getsockname()[1]

        return self.port


class Player(Base):
    def __init__(self, host: str, port: int = 50870):
        super().__init__(host, port)
        self.__playlist: Playlist = Playlist(host, port)

    def new(self, **player_args):
        self.command('new', **player_args)
        self.playlist.refresh()

    def play(self, file: str):
        self.command('play', file)
        self.playlist.refresh()

    def stream(self, file: str) -> Stream:
        return Stream(self._host, file)

    @property
    def playlist(self) -> Playlist:
        return self.__playlist
