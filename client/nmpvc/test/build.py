#!/usr/bin/env python

import sys
import json
import types
import inspect

from typing import Optional, Any

import mpv

player = mpv.MPV()

db: dict[str, dict[str, Optional[Any]]] = {
    "property": {},
    "method": {}
}

for name in list(set(dir(player))):
    try:
        attr = getattr(player, name)

    except (RuntimeError, AttributeError) as ex:
        print(f"err: {ex.args[2][1].decode()}: {ex.args[0]}", file=sys.stderr)
        continue

    if isinstance(attr, types.MethodType):
        params = inspect.getfullargspec(attr)

        _args_len = len(params.args) - (len(params.defaults) if params.defaults else -1)
        args = params.args[:_args_len]

        if 'self' in args:
            args.remove('self')

        kwargs = dict()
        for key, default in zip(params.args[_args_len:], list(params.defaults) if params.defaults else []):
            kwargs[key] = default

        db['method'][name] = {
            "help": f"{params!r}",
            "args": f"{args!r}",
            "kwargs": f"{kwargs!r}"
        }

    else:
        db['property'][name] = f"{attr!r}"

with open('mpv.json', 'w') as file:
    json.dump(db, file, indent=2)
