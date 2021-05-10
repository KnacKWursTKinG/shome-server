
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

    def send_data(self, server: str, data: Any):
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

    def run_method(self, server: str, name: str, *args, **kwargs):
        return self.send_data(
            server,
            {
                "attr": str(name),
                "args": args,
                "kwargs": kwargs
            }
        )

    def set_prop(self, server: str, prop: str, value: Any):
        return self.send_data(
            server,
            {
                "attr": str(prop),
                "value": value
            }
        )

    def get_prop(self, server: str, prop: str):
        return self.send_data(
            server,
            {
                "attr": str(prop)
            }
        )


class MPV:
    def __init__(self, *addr: tuple[str, int]):
        self.base: dict[str, MPVBase] = dict()

        for server, port in addr:
            self.base[server] = MPVBase(int(port))

    def run_method(self, name: str, *args, **kwargs):
        ...

    def __setattr__(self, name: str, value: Any):
        print(f"__setattr__ ({name=}, {value=})")
        ...

    def __getattr__(self, name: str):
        print(f"__getattr__ ({name=})")
        ...
