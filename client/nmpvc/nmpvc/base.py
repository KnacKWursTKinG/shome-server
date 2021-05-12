
import json

from typing import Any

import requests

from kwking_helper import rq  # type: ignore
from kwking_helper.thread import threaded2, ThreadData  # type: ignore


class MPVError(Exception):
    def __init__(self, status_code: int, *server):
        super().__init__(f"[{status_code}] {', '.join(server)}")
        self.status_code = status_code
        self.server = server


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

        if "application/json" in resp.headers.get('Content-Type', ''):
            return json.loads(resp.text)

        return None

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
        self.base: dict[str, MPVBase] = dict()

        self.addr = list(addr)

    @property
    def addr(self):
        return [(host, self.base[host].port) for host in self.base]

    @addr.setter
    def addr(self, addr: list[tuple[str, int]]):
        for server, port in addr:
            if server in self.base:
                del self.base[server]

            self.base[server] = MPVBase(int(port))

    def _threads(self, threads: list[tuple[str, ThreadData]]):
        ret = list()
        for server, _thread in threads:
            try:
                ret.append((server, _thread.join()))
            except Exception as ex:
                ret.append((server, ex))

        return ret

    def run(self, name: str, *args, **kwargs) -> list[tuple[str, Any]]:
        @threaded2(daemon=True)
        def _run(server: str, base: MPVBase):
            return base.run(server, name, *args, **kwargs)

        return self._threads(
            [(server, _run(server, base)) for server, base in self.base.items()]
        )

    def set(self, name: str, value: Any):
        @threaded2(daemon=True)
        def _set(server: str, base: MPVBase):
            return base.set(server, name, value)

        return self._threads(
            [(server, _set(server, base)) for server, base in self.base.items()]
        )

    def get(self, name: str):
        @threaded2(daemon=True)
        def _get(server: str, base: MPVBase):
            return base.get(server, name)

        return self._threads(
            [(server, _get(server, base)) for server, base in self.base.items()]
        )
