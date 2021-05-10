
import json
import socket

from typing import Union

import requests

from kwking_helper import rq
from kwking_helper.config import c
from kwking_helper.thread import threaded2


class PiRGB():
    """ shomeserver pi_rgb requests """
    plugin: str = 'pi_rgb'

    def __init__(self, host: str, port: int = None):
        self.host = socket.gethostbyname(host)
        self.port = int(port or c.main.getint('shomeserver', 'port'))
        self.url = f"http://{self.host}:{self.port}/api"
        self.timeout = 5

    @threaded2(daemon=True)
    def on(self, sections: list[Union[str, int]]):
        sections = list(set(map(str, sections)))
        r = requests.post(
            f"{self.url}/{self.plugin}/on",
            json={
                'sections': sections
            },
            timeout=self.timeout
        )

        if not r:
            raise rq.RQError(r)

    @threaded2(daemon=True)
    def off(self, sections: list[Union[str, int]]):
        sections = list(set(map(str, sections)))
        r = requests.post(
            f"{self.url}/{self.plugin}/off",
            json={
                'sections': sections
            },
            timeout=self.timeout
        )

        if not r:
            raise rq.RQError(r)

    @threaded2(daemon=True)
    def get(self, sections: list[Union[str, int]]) -> list[list[int]]:
        sections = list(set(map(str, sections)))
        r = requests.post(
            f"{self.url}/{self.plugin}/get",
            json={
                'sections': sections
            },
            timeout=self.timeout
        )

        if r:
            return json.loads(r.text)

        raise rq.RQError(r)

    @threaded2(daemon=True)
    def set(self, sections: list[Union[str, int]], rgbw: Union[tuple[int, ...], list[int]]):
        sections = list(set(map(str, sections)))
        r = requests.post(
            f"{self.url}/{self.plugin}/set",
            json={
                'sections': sections,
                'rgbw': rgbw
            },
            timeout=self.timeout
        )

        if not r:
            raise rq.RQError(r)

    @threaded2(daemon=True)
    def bright(self, sections: list[Union[str, int]], bright: int, _calc: str = None):
        sections = list(map(str, sections))
        threads = list()

        if _calc not in ['-', '+']:
            raise Exception("_calc should be '+' or '-' not '{_calc}'")

        def _calc_bright(_rgbw):
            old_bright = int(sum(_rgbw) / ((255 * 4) / 100))

            if _calc == '+':
                return old_bright + bright

            return old_bright - bright

        rgbw = self.get(*sections).join()

        for _section, _rgbw in zip(sections, rgbw):
            if _calc:
                bright = _calc_bright(_rgbw)

            bright = 100 if bright > 100 else 0 if bright < 0 else bright

            _rgbw = [
                round(((x + (255 - max(_rgbw))) / 255) * (bright * 2.55)) for x in _rgbw
            ]
            threads.append(self.set(_rgbw, _section))

        for t in threads:
            t.join()
