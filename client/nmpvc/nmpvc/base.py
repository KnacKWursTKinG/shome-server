
import json
import socket

from typing import Any, Union

import requests

from kwking_helper import rq  # type: ignore
from kwking_helper.thread import threaded2, ThreadData  # type: ignore


class MPV:
    def __init__(self, *addr: Union[str, tuple[str, int]], sync: bool = True):
        self._port = 50870
        self.sync = bool(sync)
        self.addr = list(addr)

    @property
    def addr(self) -> list[tuple[str, int]]:
        return self._addr

    @addr.setter
    def addr(self, addr: list[Union[str, tuple[str, int]]]):
        self._addr = list()

        for _addr in addr:
            if isinstance(_addr, str):
                self._addr.append((socket.gethostbyname(_addr), self._port))
            elif isinstance(_addr, tuple):
                self._addr.append((socket.gethostbyname(_addr[0]), _addr[1]))
            else:
                raise ValueError("'addr' should contain tuples with host and port")

    def _url(self, addr: tuple[str, int]):
        return "http://{}:{}/api/nmpv/player".format(*addr)

    def _send(self, addr: tuple[str, int], data: Any):
        resp = requests.post(
            self._url(addr),
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

    @threaded2(daemon=True)
    def _run(self, addr: tuple[str, int], name: str, *args, **kwargs):
        return self._send(
            addr,
            {
                "sync": ...,  # @todo
                "attr": str(name),
                "args": args,
                "kwargs": kwargs
            }
        )

    @threaded2(daemon=True)
    def _set(self, addr: tuple[str, int], prop: str, value: Any):
        return self._send(
            addr,
            {
                "sync": ...,  # @todo
                "attr": str(prop),
                "value": value
            }
        )

    @threaded2(daemon=True)
    def _get(self, addr: tuple[str, int], prop: str):
        return self._send(
            addr,
            {
                "sync": ...,  # @todo
                "attr": str(prop)
            }
        )

    def _threads(self, threads: list[tuple[tuple[str, int], ThreadData]]):
        ret = list()
        for server, _thread in threads:
            try:
                ret.append((server, _thread.join()))
            except Exception as ex:
                ret.append((server, ex))

            del _thread

        return ret

    def run(self, name: str, *args, **kwargs) -> list[tuple[str, Any]]:
        return self._threads(
            [(addr, self._run(addr, name, *args, **kwargs)) for addr in self.addr]
        )

    def set(self, name: str, value: Any):
        return self._threads(
            [(addr, self._set(addr, name, value)) for addr in self.addr]
        )

    def get(self, name: str):
        return self._threads(
            [(addr, self._get(addr, name)) for addr in self.addr]
        )
