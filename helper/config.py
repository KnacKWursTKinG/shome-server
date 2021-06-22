""" Simple Configuration System for handling multiple configparser
(.ini) files in one class, + add optionally environment
section (custom or default) [default: dict(os.environ)]

* support `shell one liners`


"""

from __future__ import annotations

import os
import re
import subprocess as sp

from configparser import ConfigParser, ExtendedInterpolation
from typing import Union

from . import rq


class ExtendedInterpolation(ExtendedInterpolation):
    RE_SHELL = re.compile(r'^`(?P<command>.*)`$')
    RE_EXTEND = re.compile(r'.*(?P<replace>\${(?P<section>.*):(?P<option>.*)}).*')

    def before_get(self, parser, section, option, value, defaults):
        match_extend = re.match(self.RE_EXTEND, value)

        if match_extend:
            value = value.replace(
                match_extend.group('replace'),
                parser.get(
                    match_extend.group('section'),
                    match_extend.group('option')
                )
            )

        match_shell = re.match(self.RE_SHELL, value)

        if match_shell:
            # TODO catch sp.CalledProcessError
            # TODO pipe stderr to stdout
            value = sp.check_output(
                match_shell.group('command'), shell=True
            ).rstrip().decode('utf-8')

        return super().before_get(parser, section, option, value, defaults)


class c:
    db: rq.DBServer = None

    @classmethod
    def read(cls, file: Union[str, list[str]], namespace: str = 'main',
             enable_env: bool = False, _env: dict[str, str] = None):
        """ read and set ini file """

        if namespace == 'db':
            raise ValueError(f"{namespace} is locked")

        try:
            ini = getattr(cls, namespace)
        except AttributeError:
            setattr(cls, namespace, ConfigParser(interpolation=ExtendedInterpolation()))
            ini = getattr(cls, namespace)

            if enable_env:
                ini.read_dict({'env': dict(os.environ) if not _env else dict(_env)})

        ini.read(file)

    @classmethod
    def read_dict(cls, data: dict[str, dict[str, str]], namespace: str = 'main',
                  enable_env: bool = False, _env: dict[str, str] = None):

        if namespace == 'db':
            raise ValueError(f"{namespace} is locked")

        try:
            ini = getattr(cls, namespace)
        except AttributeError:
            setattr(cls, namespace, ConfigParser(interpolation=ExtendedInterpolation()))
            ini = getattr(cls, namespace)

            if enable_env:
                ini.read_dict({'env': dict(os.environ) if not _env else dict(_env)})

        ini.read_dict(data)

    @classmethod
    def dict(cls, namespace: str = 'main') -> dict[str, dict[str, str]]:
        if namespace == 'db':
            raise ValueError(f"{namespace} is locked")

        return getattr(cls, namespace, None).__dict__['_sections']
