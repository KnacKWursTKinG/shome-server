
from __future__ import annotations

import os
import socket
import time
import mimetypes

from threading import Thread
from multiprocessing import Process
from typing import Union

from flask import Flask, Response, request

from kwking_helper.logging import CL


__all__ = ['Stream']


# TODO: add support for multiple hosts (quit only after last request in hosts)
# TODO: add support for youtube
class Stream(Process):
    Queue: set[Process] = set()

    def __init__(self, host: Union[str, list[str]], file: str, log_level: str = 'warning'):
        super().__init__()
        self.daemon = True
        self.id = id(self)
        self.name = f"stream-{self.id}"

        self.file = os.path.expanduser(file)

        if not os.path.isfile(self.file):
            raise FileNotFoundError(self.file)

        self.mimetype = mimetypes.guess_type(self.file)
        self.rule = f"/{self.id}"

        self.hosts = [host] if not isinstance(host, list) else host
        self.hosts = [socket.gethostbyname(_) for _ in self.hosts]
        self.host = self.hosts[0] if len(self.hosts) == 1 else '0.0.0.0'
        self.port = 0
        self.chunk_size = 1024 * 1024

        self.logger = CL(
            log_level, f"{self.name}"
        )

    def __del__(self):
        if self in Stream.Queue:
            Stream.Queue.remove(self)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.logger.debug(f"[__exit__] {args=}")
        self.__del__()

    def start(self):
        self.generate_port()
        super().start()
        Stream.Queue.add(self)

    @property
    def url(self):
        return f"http://{self.host}:{self.port}{self.rule}"

    def generate_port(self):
        with socket.create_server(('localhost', 0)) as s:
            self.port = s.getsockname()[1]

    def run(self):
        server = Flask(self.name)
        hosts = self.hosts

        @server.after_request
        def quit(response: Response):
            self.logger.debug(f"[after_request] {request.host=}, {request.host_url}")
            # TODO: remove host from hsots
            ...

            def _exit():
                time.sleep(1)
                os._exit(0)

            Thread(target=_exit).start()

            return response

        @server.route(self.rule)
        def stream():
            def generator():
                with open(self.file, 'rb') as f:
                    while (data := f.read(self.chunk_size)):
                        yield data

            return Response(
                generator(), mimetype=self.mimetype
            )

        server.run(self.host, self.port)
