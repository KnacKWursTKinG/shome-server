
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

    def __init__(self, file: str, hosts: Union[str, list[str]], log_level: str = 'warning'):
        super().__init__()
        self.daemon = True
        self.id = id(self)
        self.name = f"stream-{self.id}"

        self.file = os.path.expanduser(file)

        if not os.path.isfile(self.file):
            raise FileNotFoundError(self.file)

        self.mimetype = mimetypes.guess_type(self.file)[0]
        self.rule = f"/{self.id}"

        _hosts = set([hosts] if not isinstance(hosts, list) else hosts)
        self.hosts: list[str] = [socket.gethostbyname(_) for _ in _hosts]
        self.host = '0.0.0.0' if len(self.hosts) > 1 else self.hosts[0]
        self.port = 0
        self.chunk_size = 1024 * 1024

        self.logger = CL(
            log_level, f"{self.name}"
        )

    def __del__(self):
        if self.is_alive():
            self.kill()

        if self in Stream.Queue:
            Stream.Queue.remove(self)

    def __enter__(self):
        self.start()
        self.join(.1)
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
        import logging
        server = Flask(self.name)
        self.hosts_server_quit = self.hosts
        logging.getLogger('werkzeug').disabled = True
        os.environ['WERKZEUG_RUN_MAIN'] = 'true'

        @server.after_request
        def quit(response: Response):
            try:
                self.logger.debug(
                    f"remove {request.remote_addr!r} from {self.hosts_server_quit!r}"
                )
                self.hosts_server_quit.remove(request.remote_addr)
            except ValueError:
                if request.remote_addr == '127.0.0.1':
                    self.logger.debug(
                        f"ValueError: remove '127.0.1.1' from {self.hosts_server_quit!r}"
                    )
                    self.hosts_server_quit.remove('127.0.1.1')

            def _exit():
                time.sleep(1)
                os._exit(0)

            if not self.hosts_server_quit:
                self.logger.debug(f"quit server ({self.host=}, {self.port=})")
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

        self.logger.debug(f"server start on ({self.host=}, {self.port=})")
        server.run(self.host, self.port)
