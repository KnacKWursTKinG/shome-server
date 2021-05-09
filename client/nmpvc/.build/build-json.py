#!/usr/bin/env python

import sys
import json
import types
import inspect

from typing import Optional, Any

import mpv

player = mpv.MPV()

db: dict[str, dict[str, Optional[Any]]] = {
    "method": {},
    "property": {}
}

for name in list(set(dir(player))):
    try:
        attr = getattr(player, name)

    except (RuntimeError, AttributeError) as ex:
        print(f"err: {ex.args[2][1].decode()}: {ex.args[0]}", file=sys.stderr)
        continue

    if isinstance(attr, types.MethodWrapperType):
        print(f"skip method-wrapper type: {attr!r}")
        continue

    if isinstance(attr, (types.MethodType, types.FunctionType)):
        params = inspect.getfullargspec(attr)

        #_args_len = len(params.args) - (len(params.defaults) if params.defaults else -1)
        #args = params.args[:_args_len]

        #if 'self' in args:
        #    args.remove('self')

        #kwargs = dict()
        #for key, default in zip(params.args[_args_len:], list(params.defaults) if params.defaults else []):
        #    kwargs[key] = default

        defaults = list()
        for _default in list(params.defaults) if params.defaults else []:
            defaults.append(f"{_default!r}")

        kwonlydefaults = dict()
        for _key, _value in params.kwonlydefaults.items() if params.kwonlydefaults else {}.items():
            kwonlydefaults[_key] = f"{_value!r}"

        db['method'][name] = {
            "args": params.args,
            "varargs": params.varargs,
            "varkw": params.varkw,
            "defaults": defaults,
            "kwonlyargs": params.kwonlyargs,
            "kwonlydefaults": kwonlydefaults,
            "annotations": params.annotations
        }

    else:
        db['property'][name] = f"{attr!r}"

with open('mpv.json', 'w') as file:
    json.dump(db, file, indent=2)
