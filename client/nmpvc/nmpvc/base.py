
import json
import socket

from typing import Any

import requests

from kwking_helper import rq


class MPVBase:
    def __init__(self, port: int = 50870):
        self.port = port

    def url(self, server: str):
        return f"http://{server}:{self.port}/api/nmpv/player"

    def send(self, server: str, data: Any):
        resp = requests.post(
            self.url(server),
            json.loads(data),
            headers={
                'Content-Type': 'application/json'
            }
        )

        if resp.status_code != 200:
            raise rq.RQError(resp)

        return json.loads(resp.text) if "application/json" in resp.headers.get('Content-Type') else None

    def run(self, server: str, name: str, *args, **kwargs):
        return self.send(
            server,
            {
                "attr": str(name),
                "args": args,
                "kwargs": kwargs
            }
        )

    def set(self, server: str, prop: str, value: Any):
        return self.send(
            server,
            {
                "attr": str(prop),
                "value": value
            }
        )

    def get(self, server: str, prop: str):
        return self.send(
            server,
            {
                "attr": str(prop)
            }
        )


class MPV:
    def __init__(self, *addr: tuple[str, int]):
        self._addr = list(addr)
        self.base: dict[str, MPVBase] = dict()

    @property
    def addr(self):
        return self._addr

    @addr.setter
    def addr(self, addr: list[tuple[str, int]]):
        for server, port in addr:
            if server in self.base:
                del self.base[server]

            self.base[server] = MPVBase(int(port))

    def run(self, name: str, *args, **kwargs):
        ...

    def set(self, name: str, value: Any):
        ...

    def get(self, name: str):
        ...
