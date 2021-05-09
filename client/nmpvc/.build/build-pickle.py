#!/usr/bin/env python

import sys
import dill as pickle
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

        defaults = list()
        for _default in list(params.defaults) if params.defaults else []:
            defaults.append(_default)

        kwonlydefaults = dict()
        for _key, _value in params.kwonlydefaults.items() if params.kwonlydefaults else {}.items():
            kwonlydefaults[_key] = _value

        # test pickling
        try:
            pickle.dumps(params)
        except ValueError as ex:
            print(f"{ex!r} ({params!r})", file=sys.stderr)
            continue

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
        try:
            pickle.dumps(attr)
        except ValueError as ex:
            print(f"{ex!r} ({attr!r})", file=sys.stderr)
            continue

        db['property'][name] = attr

with open('mpv.pickle', 'wb') as file:
    pickle.dump(db, file)
