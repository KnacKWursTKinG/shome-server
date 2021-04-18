#!/usr/bin/env python

import socket
import pickle
import typing

import click


def client(data: tuple[str, typing.Optional[tuple], typing.Optional[dict]],
           addr: tuple[str, int] = ('localhost', 5001)):

    with socket.create_connection(addr) as s:
        s.sendall(
            pickle.dumps(
                data
            )
        )

        return pickle.loads(s.recv(1024 * 100))


@click.group()
def cli():
    pass


@cli.command('play')
@click.argument('filename')
def _play(filename: str):
    _ret = client(('play', (filename, ), {}))

    if _ret:
        print(f"{_ret!r}")


@cli.command('get')
@click.argument('get')
def _get(get: str):
    _ret = client((get, None, None))

    if isinstance(_ret, list):
        for _part in _ret:
            print(_part)

    else:
        print(f"{_ret!r}")


if __name__ == "__main__":
    cli()
