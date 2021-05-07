#!/usr/bin/env python

import types
import inspect

from kwking_helper.logging import CL


TemplateClassBase = """

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
"""

TemplateClassMPVProperty = """


class MPVProperty(MPVBase):\
"""

TemplateClassMPVMethod = """


class MPVMethod(MPVBase):\
"""

TemplateClassMPV = """

class MPV(MPVProperty, MPVMethod):
    pass\
"""

TemplateProperty = """

    @property
    def {name}(self):
        return self._get_prop('{name}')

    @{name}.setter
    def {name}(self, value):
        return self._set_prop('{name}', value)\
"""

TemplateMethod = """

    def {name}(self, {args}, *{varargs}, **{varkw}):
        return self._run_method('{name}', {args}, *{varargs}, **{varkw})\
"""


class BuildMPV:
    def __init__(self):
        self.logger = CL(
            'debug', __name__, _format="[{level}] {message}"
        )

        self.code_base = TemplateClassBase
        self.code_property = TemplateClassMPVProperty
        self.code_method = TemplateClassMPVMethod
        self.code_mpv = TemplateClassMPV

    def run(self):
        import mpv

        player = mpv.MPV()

        for name in list(set(dir(player))):
            try:
                attr = getattr(player, name)

            except (RuntimeError, AttributeError) as ex:
                self.logger.error(f"{ex.args[2][1].decode()}: {ex.args[0]}")
                continue

            if name[0] == '_':
                continue

            if name in ['quit', 'terminate', '3dlut_size']:
                continue

            if isinstance(attr, types.MethodType):
                _params = inspect.getfullargspec(attr)

                if _params.args:
                    if _params.args[0] != 'self':
                        _params.args.insert(0, 'self')
                else:
                    _params.args.append('self')

                self.code_method += TemplateMethod.format(
                    name=name,
                    args=', '.join(_params.args[1:len(_params.defaults) if _params.defaults else -1]),
                    varargs=_params.varargs or 'args',
                    varkw=_params.varkw or 'kwargs'
                )

            else:
                self.code_property += TemplateProperty.format(name=name)

    def save(self, out: str):
        with open(out, 'w') as file:
            file.write(self.code_base + self.code_property + self.code_method + self.code_mpv)


if __name__ == "__main__":
    build = BuildMPV()
    build.run()
    build.save('_mpv.py')
