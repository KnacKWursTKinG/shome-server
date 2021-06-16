
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


class StreamLocal(Process):
    Queue: set[StreamLocal] = set()

    def __init__(self, file: str, hosts: list[str], log_level: str = 'warning'):
        super().__init__()
        self.daemon = True
        self.id = id(self)
        self.name = f"stream-{self.id}"

        self.file = os.path.expanduser(file)
        self.hosts: list[str] = [socket.gethostbyname(_) for _ in list(set(hosts))]

        if not os.path.isfile(self.file):
            raise FileNotFoundError(self.file)

        self.logger = CL(
            log_level, f"{self.name}"
        )

        self._chunk_size = 1024 * 1024
        self._mimetype = mimetypes.guess_type(self.file)[0]
        self._rule = f"/{self.id}"
        self._host = '0.0.0.0'
        self._port = 0

    def __del__(self):
        if self.is_alive():
            self.kill()

        if self in StreamLocal.Queue:
            StreamLocal.Queue.remove(self)

    def __enter__(self):
        self.start()
        self.join(.1)
        return self

    def __exit__(self, *args):
        self.logger.debug(f"[__exit__] {args=}")
        self.__del__()

    def start(self):
        self._generate_port()
        super().start()
        StreamLocal.Queue.add(self)

    @property
    def url(self):
        return f"http://{self._host}:{self._port}{self._rule}"

    def _generate_port(self):
        with socket.create_server(('localhost', 0)) as s:
            self._port = s.getsockname()[1]

    def run(self):
        import logging

        self.hosts_server_quit = self.hosts

        server = Flask(self.name)

        # disable flask logging stuff
        logging.getLogger('werkzeug').disabled = True
        os.environ['WERKZEUG_RUN_MAIN'] = 'true'

        @server.after_request
        def quit(response: Response):
            try:
                self.hosts_server_quit.remove(request.remote_addr)
            except ValueError as ex:
                if request.remote_addr == '127.0.0.1':
                    self.hosts_server_quit.remove('127.0.1.1')
                else:
                    raise ex

            def _exit():
                time.sleep(1)
                os._exit(0)

            if not self.hosts_server_quit:
                self.logger.debug(f"quit server: {self.url}")
                Thread(target=_exit).start()

            return response

        @server.route(self._rule)
        def stream():
            def generator():
                with open(self.file, 'rb') as f:
                    while (data := f.read(self._chunk_size)):
                        yield data

            return Response(
                generator(), mimetype=self._mimetype
            )

        self.logger.debug(f"server started: {self.url}")
        server.run(self._host, self._port)
