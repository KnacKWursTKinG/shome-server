
import json
import socket

import requests

from kwking_helper import rq


class MPVBase:
    def __init__(self, host, port = 50870):
        self.url = f"http://{socket.gethostbyname(host)}:{port}/api/nmpv/player"

    def send_data(self, data):
        resp = requests.post(
            self.url,
            json.loads(data),
            headers={
                'Content-Type': 'application/json'
            }
        )

        if resp.status_code != 200:
            raise rq.RQError(resp)

        return json.loads(resp.text) if "application/json" in resp.headers.get('Content-Type') else None

    def run_method(self, name: str, *args, **kwargs):
        return self.send_data({
            "attr": str(name),
            "args": args,
            "kwargs": kwargs
        })

    def set_prop(self, prop: str, value):
        return self.send_data({
            "attr": str(prop),
            "value": value
        })

    def get_prop(self, prop: str):
        return self.send_data({
            "attr": str(prop)
        })


class MPV:
    def __init__(self, *addr: tuple[str, int]):
        self.base: dict[str, MPVBase] = dict()

        for server, port in addr:
            self.base[server] = MPVBase(server, int(port))
