
import socket
import sys

from dataclasses import dataclass, field
from typing import Optional

import click

from click_aliases import ClickAliasedGroup

from kwking_helper.config import c
from kwking_helper.logging import CL
from kwking_helper.thread import ThreadData

from pirgb import config
from pirgb.pirgb import PiRGB


LOG_FORMAT = "[{level}] {message}"


@dataclass
class Obj:
    logger: CL
    port: Optional[int] = None
    pi: set[tuple[str, str]] = field(default_factory=set)
    hosts: set[str] = field(default_factory=set)

    def sections(self, host) -> list[str]:
        sections = set()
        for _host, _section in self.pi:
            if host == _host:
                sections.add(_section)
        return list(sections)


# <<- click.group: cli
@click.group(cls=ClickAliasedGroup)
@click.option('-l', '--log-level', type=click.Choice(CL.LEVELS, False),
              default="info", show_default=True,
              help="Change logging level")
@click.pass_context
def cli(ctx, **kwargs):
    """ Client (gui&cli) for shomeserver plugin control. """
    c.main.set('pirgb', 'log_level', kwargs['log_level'])
    ctx.obj = Obj(
        CL(kwargs['log_level'], 'click', _format=LOG_FORMAT)
    )
# ->>


# <<- cli.command: 'gui', 'g'
@cli.command('gui', aliases=['gui', 'g'])
@click.option('-g', '--gui', metavar="<webview>", default='qt', show_default=True,
              help="change default webview to use (qt, gtk)")
@click.pass_obj
def gui(obj: Obj, gui: str):
    """ Flask GUI """
    import os
    import threading

    from pirgb.server import server

    _platform = config.platform()
    obj.logger.debug(f"running flask gui on {_platform}")

    if _platform == 'ubuntu-phablet':
        sock = socket.socket()
        sock.bind(('localhost', 0))
        port = sock.getsockname()[1]
        sock.close()

        thread = threading.Thread(target=server.run, kwargs={'port': port}, daemon=True)
        thread.start()

        os.system("webapp-container 'http://localhost:{}/'".format(port))
        sys.exit(0)

    if _platform == 'Linux':
        import webview

        webview.create_window('PiRGB Flask GUI', server)
        webview.start(debug=bool(obj.logger.level == 'debug'), gui=gui)
# ->>


# <<- cli.group: term
# TODO add autocompletion for '--pi' option (list hostnames and sections)
# NOTE: parse config pi_rgb for autocompetion
@cli.group('cli', aliases=['cli', 'c'], chain=True, cls=ClickAliasedGroup)
@click.option('-p', '--pi', metavar="<host>[:<section>]", multiple=True,
              help="Pi to control [default-section: 1] [multiple: True]")
@click.option('--port', type=int, default=c.main.getint('shomeserver', 'port'),
              show_default=True, metavar="<port>",
              help="Change default shomeserver port")
@click.pass_obj
def term(obj: Obj, **kwargs):
    """ Terminal Client [chain: True] """
    obj.logger.debug("[term] running terminal client")
    obj.port = kwargs['port']

    for pi in kwargs['pi']:
        _host, _section = tuple(pi.split(':') + ["1"])[:2]
        obj.pi.add((_host, _section))
        obj.hosts.add(_host)

    obj.logger.debug(f"[term] {obj.port=}")
    obj.logger.debug(f"[term] {obj.pi=}")
    obj.logger.debug(f"[term] {obj.hosts=}")
# ->>


# <<- term.command: 'set', 's'
@term.command('set', aliases=['set', 's'])
@click.option('-w', '--ww', type=click.IntRange(0, 100), metavar="<range>",
              help="Set the warm white value from 0 to 100% [default: auto]")
@click.argument('r', type=click.IntRange(0, 255), metavar="<r>")
@click.argument('g', type=click.IntRange(0, 255), metavar="<g>")
@click.argument('b', type=click.IntRange(0, 255), metavar="<b>")
@click.pass_obj
def term_set(obj: Obj, **kwargs):
    """ Set RGBW for pi (ww auto handling) """
    threads: list[tuple[ThreadData, str]] = list()
    rgbw = [kwargs['r'], kwargs['g'], kwargs['b']]

    if not kwargs['ww']:
        kwargs['ww'] = max(rgbw) if len(set(rgbw)) == 1 else 0

    rgbw.append(kwargs['ww'])
    obj.logger.debug(f"[set] {rgbw=}")

    for host in obj.hosts:
        try:
            threads.append((PiRGB(host).set(sections=obj.sections(host), rgbw=rgbw), host))
        except socket.gaierror:
            obj.logger.critical(f"[set] server offline: {host}")

    for _t, host in threads:
        try:
            _t.join()
        except Exception as ex:
            obj.logger.error(f"[set] {host}: {ex!r}")
# ->>


# <<- term.command: 'get'
@term.command('get', aliases=['get', 'g'])
@click.pass_obj
def term_get(obj: Obj):
    """ Get RGBW for Sections """
    threads: list[tuple[ThreadData, str, list[str]]] = list()

    for host in obj.hosts:
        sections = obj.sections(host)

        try:
            threads.append((PiRGB(host).get(sections=sections), host, sections))
        except socket.gaierror:
            obj.logger.critical(f"[get] server offline: {host}")

    for _t, host, sections in threads:
        try:
            ret = _t.join()
        except Exception as ex:
            obj.logger.error(f"[get] {host}: {ex!r}")

        if ret:
            for _section, _rgbw in zip(sections, ret):
                obj.logger.info(f"{host}:{_section} {_rgbw}")
# ->>


# <<- term.command: 'on'
@term.command('on')
@click.pass_obj
def term_on(obj: Obj):
    """ RGBW On """
    threads: list[tuple[ThreadData, str]] = list()

    for host in obj.hosts:
        try:
            threads.append((PiRGB(host).on(sections=obj.sections(host)), host))
        except socket.gaierror:
            obj.logger.critical(f"[on] server offline: {host}")

    for _t, host in threads:
        try:
            _t.join()
        except Exception as ex:
            obj.logger.error(f"[on] {host}: {ex!r}")
# ->>


# <<- term.command: 'off'
@term.command('off')
@click.pass_obj
def term_off(obj: Obj):
    """ RGBW Off """
    threads: list[tuple[ThreadData, str]] = list()

    for host in obj.hosts:
        try:
            threads.append((PiRGB(host).off(sections=obj.sections(host)), host))
        except socket.gaierror:
            obj.logger.critical(f"[off] server offline: {host}")

    for _t, host in threads:
        try:
            _t.join()
        except Exception as ex:
            obj.logger.error(f"[off] {host}: {ex!r}")
# ->>


# <<- term.command: 'bright', 'b'
@term.command('bright', aliases=['bright', 'b'])
@click.option('-i', '--increase', is_flag=True, default=False, help="increase brightness")
@click.option('-d', '--decrease', is_flag=True, default=False, help="decrease brightness")
@click.argument('brightness', type=click.IntRange(0, 100), metavar="<brightness>")
@click.pass_obj
def term_bright(obj: Obj, **kwargs):
    """ Change Brightness for RGBW (in '%') """
    threads: list[tuple[ThreadData, str]] = list()
    _calc = None

    if kwargs['increase']:
        _calc = '+'

    if kwargs['decrease']:
        if _calc:
            obj.logger.error("[bright] increase flag already set")
            sys.exit(1)

        _calc = '-'

    for host in obj.hosts:
        try:
            threads.append(
                (
                    PiRGB(host).bright(
                        sections=obj.sections(host),
                        bright=kwargs['brightness'],
                        _calc=_calc
                    ),
                    host
                )
            )
        except socket.gaierror:
            obj.logger.critical(f"[bright] server offline: {host}")

    for _t, host in threads:
        try:
            _t.join()
        except Exception as ex:
            obj.logger.error(f"[on] {host}: {ex!r}")
# ->>
