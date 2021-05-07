
import types
import inspect

from kwking_helper.logging import CL


Code = """

import json

import requests

from kwking_helper import rq


class MPV:
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
        })
"""

TemplateProperty = """

    @property
    def {name}(self):
        return self._get_prop({name})

    @{name}.setter
    def {name}(self, value):
        return self._set_prop('{name}', value)
"""

TemplateMethod = """

    def {name}({args}, *{varargs}, **{varkw}):
        return self._run_method({name}, {args}, *{varargs}, **{varkw})
"""



class BuildMPV:
    def __init__(self):
        self.logger = CL(
            'debug', __name__, _format="[{level}] {message}"
        )

        self.code = Code

    def run(self):
        import mpv

        player = mpv.MPV()

        for name in dir(player):
            try:
                attr = getattr(player, name)
            except RuntimeError as ex:
                self.logger.error(f"{ex.args[2][1].decode()}: {ex.args[0]}")
                continue

            if name[0] == '-':
                continue

            if name in ['quit', 'terminate']:
                continue

            if isinstance(attr, types.MethodType):
                _params = inspect.getfullargspec(attr)

                self.code += TemplateMethod.format(
                    name=name,
                    args=', '.join(_params.args),
                    varargs=_params.varargs or 'args',
                    varkw=_params.varkw or 'kwargs'
                )

            else:
                self.code += TemplateProperty.format(name=name)

    def save(self, out: str):
        with open(out, 'w') as file:
            file.write(self.code)


if __name__ == "__main__":
    build = BuildMPV()
    build.run()
    build.save('nmpvc.py')
