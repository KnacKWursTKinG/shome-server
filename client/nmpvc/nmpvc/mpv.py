
import json
import socket

import requests

from kwking_helper import rq


class MPVBase:
    def __init__(self, host, port = 50870):
        self.url = f"http://{socket.gethostbyname(host)}:{port}/api/nmpv/player"

    def _send_data(self, data):
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

    def _run_method(self, name: str, *args, **kwargs):
        return self._send_data({
            "attr": str(name),
            "args": args,
            "kwargs": kwargs
        })

    def _set_prop(self, prop: str, value):
        return self._send_data({
            "attr": str(prop),
            "value": value
        })

    def _get_prop(self, prop: str):
        return self._send_data({
            "attr": str(prop)
        })\
