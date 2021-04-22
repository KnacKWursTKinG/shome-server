#!/usr/bin/env python
# Test Server

import socket
import pickle
import types
import typing

from mpv import MPV

from kwking_helper import thread


Player: MPV = None

DEFAULTS = {
    'ytdl': True
}


@thread(daemon=False)
def run(_conn, _addr, data: bytes):
    global Player

    attr: typing.Union[str, typing.Any]
    args: typing.Optional[tuple]
    kwargs: typing.Optional[dict]
    _return: typing.Any = None
    defaults = DEFAULTS

    attr, args, kwargs = pickle.loads(data)

    print(f"player.{attr}({args=}, {kwargs=})")

    # TODO: check if Player is terminated/closed
    ...

    if Player is None or attr == 'new':
        if attr == 'new':
            if Player is not None:
                Player.quit(0)
                Player.terminate()
                del Player

            if isinstance(kwargs, dict):
                defaults = {**defaults, **kwargs}

        Player = MPV(**defaults)

    if attr == 'new':
        return _conn.sendall(pickle.dumps(_return))

    attr = getattr(Player, attr)
    print(f"{type(attr)=}; {attr=}")
    #print(f"{isinstance(attr, types.MethodType)=}")

    if isinstance(attr, types.MethodType) and isinstance(args, tuple) and isinstance(kwargs, dict):
        _return = attr(*args, **kwargs)

    else:
        print(f"{attr=}")
        _return = attr

    return _conn.sendall(pickle.dumps(_return))


with socket.create_server(('localhost', 5001)) as server:
    server.listen()

    while True:
        print('-' * 80)
        conn, addr = server.accept()

        run(conn, addr, conn.recv(1024 * 100)).join()

        conn.close()
