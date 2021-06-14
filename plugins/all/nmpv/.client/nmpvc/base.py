
import json
import socket
import time

from typing import Any, Union, Optional

import requests

from kwking_helper import rq  # type: ignore
from kwking_helper.thread import threaded2, ThreadData  # type: ignore


# @todo: enable/disable sync, set delay (ts) value
class MPV:
    def __init__(self, *addr: Union[str, tuple[str, int]], sync: bool = False):
        self._port = 50870
        self.sync = bool(sync)
        self.addr = list(addr)  # type: ignore

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
            json.dumps(data),
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
    def _run(self, sync: Optional[float], addr: tuple[str, int], name: str, *args, **kwargs):
        data = {
            "sync": sync,
            "attr": str(name),
            "args": args,
            "kwargs": kwargs
        }

        return self._send(addr, data)

    @threaded2(daemon=True)
    def _set(self, sync: Optional[float], addr: tuple[str, int], prop: str, value: Any):
        data = {
            "sync": sync,
            "attr": str(prop),
            "value": value
        }

        return self._send(addr, data)

    @threaded2(daemon=True)
    def _get(self, sync: Optional[float], addr: tuple[str, int], prop: str):
        data = {
            "sync": sync,
            "attr": str(prop)
        }

        return self._send(addr, data)

    def _threads(self, threads: list[tuple[str, ThreadData]]) -> list[tuple[str, Any]]:
        ret = list()
        for server, _thread in threads:
            try:
                ret.append((server, _thread.join()))
            except Exception as ex:
                ret.append((server, ex))

            del _thread

        return ret

    def run(self, name: str, *args, **kwargs) -> list[tuple[str, Any]]:
        sync = time.time() + 1 if self.sync else None

        return self._threads(
            [(f"{addr[0]}:{addr[1]}", self._run(sync, addr, name, *args, **kwargs)) for addr in self.addr]
        )

    def set(self, name: str, value: Any) -> list[tuple[str, Any]]:
        sync = time.time() + 1 if self.sync else None

        return self._threads(
            [(f"{addr[0]}:{addr[1]}", self._set(sync, addr, name, value)) for addr in self.addr]
        )

    def get(self, name: str) -> list[tuple[str, Any]]:
        sync = time.time() + 1 if self.sync else None

        return self._threads(
            [(f"{addr[0]}:{addr[1]}", self._get(sync, addr, name)) for addr in self.addr]
        )
