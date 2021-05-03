#!/usr/bin/env python

import json
import time
import threading

import click
import requests

from click_aliases import ClickAliasedGroup

from kwking_helper.thread import threaded2, ThreadData


THREAD_LOCK = threading.Lock()


@click.group(cls=ClickAliasedGroup)
def cli():
    """ Test Client (shomeserver test plugin) """
    pass


@cli.command('sync', aliases=['sync', 's'])
@click.option('-h', '--host', multiple=True, default='localhost', show_default=True,
              help="shomeserver host [multiple: True]")
@click.option('-p', '--port', type=int, default=50870, show_default=True,
              help="shomeserver port")
@click.option('-d', '--delay', type=float, defalut=1.0, show_default=True,
              help="delay (added to time.time timestamp)")
def sync(host: tuple[str, ...], port: int, delay: float):
    """ Sync (timestamp test) """
    def t_success(_, r: requests.Response):
        with THREAD_LOCK:
            click.echo(f"[{r.url}] {json.loads(r.text)}")

    def t_error(_, ex: Exception):
        with THREAD_LOCK:
            click.echo(f"err: {ex!r}", err=True)


    @threaded2(False, t_success, t_error)
    def __thread(host: str, timestamp: float):
        r = requests.get(
            f"http://{host}:{port}/api/test/sync",
            params={'time': timestamp}
        )

        if r:
            return r

        raise Exception(f"err: {r!r}, {r.text or None}")

    ts: float = time.time() + delay

    with THREAD_LOCK:
        click.echo(f"Send {ts=} to {', '.join(list(host))}", err=True)

    for _host in list(host):
        __thread(_host, ts)


if __name__ == "__main__":
    cli()
