#!/usr/bin/env python
# Test Server

import socket
import pickle
import types
import typing

from mpv import MPV, ShutdownError

from kwking_helper import thread


Player: MPV = None

defaults = {
    'ytdl': True
}


@thread(daemon=False, log_level="debug")
def run(_conn, _addr, data: bytes):
    global Player

    attr: typing.Union[str, typing.Any]
    args: typing.Optional[tuple]
    kwargs: typing.Optional[dict]
    _return: typing.Any = None

    attr, args, kwargs = pickle.loads(data)

    print(f"player.{attr}({args=}, {kwargs=})")

    if Player is None:
        Player = MPV(**defaults)

    attr = getattr(Player, attr)
    print(f"{type(attr)=}; {attr=}")
    #print(f"{isinstance(attr, types.MethodType)=}")

    if isinstance(attr, types.MethodType) and isinstance(args, tuple) or isinstance(kwargs, dict):
        _return = attr(*args or tuple(), **kwargs or dict())

    else:
        print(f"{attr=}")
        _return = attr

    _conn.sendall(pickle.dumps(_return))


with socket.create_server(('localhost', 5001)) as server:
    server.listen()

    while True:
        print('-' * 80)
        conn, addr = server.accept()

        run(conn, addr, conn.recv(1024 * 100)).join()

        conn.close()
