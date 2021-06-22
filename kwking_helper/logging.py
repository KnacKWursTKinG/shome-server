""" A simple logging method (color, uses click.echo and click.style) """

import os
import time

from typing import Any, Optional

from click import echo, style


DEFAULT_FORMAT = "[{level}] [{name}] {message}"
"""
Possible Formats
----------------
    level : logging level
    name : logger name or what ever you set
    message : actual message to show
    time : timestamp (default for _file write)
"""
DEFAULT_FORMAT_FILE = "{time}: [{level}] [{name}] {message}"

COLORS: dict[str, dict[str, Any]] = {
    'debug': {
        'fg': 'black',
        'bold': True
    }, 'info': {
        'fg': 'white',
        'bold': True
    }, 'warning': {
        'fg': 'yellow',
        'bold': False
    }, 'error': {
        'fg': 'red',
        'bold': False
    }, 'critical': {
        'fg': 'red',
        'bold': True,
        'blink': True
    }, 'name': {
        'fg': 'cyan',
        'bold': False
    }, 'message': {
        'bold': False
    }
}


class ClickLogger:
    LEVELS = [
        'debug',
        'info',
        'warning',
        'error',
        'critical',
        'silent'
    ]

    def __init__(self, level: str, name: str, _file: str = None, _file_force_color: bool = True,
                 _stream: bool = True, _format: str = DEFAULT_FORMAT,
                 _format_file: str = DEFAULT_FORMAT_FILE, _color: bool = True):

        self.level = level.lower()
        self._format = str(_format)
        self._format_file = str(_format_file)
        self.color = dict(COLORS) if _color else {}
        self.name = name

        if _file:
            self._file = os.path.expanduser(_file) if level != 'silent' else None
        else:
            self._file = None

        self._file_force_color = _file_force_color
        self._stream = bool(_stream)

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level: str):
        assert level in self.LEVELS, "Wrong log-level '{!s}'".format(level)
        self._level = level

    @property
    def level_index(self):
        return self.LEVELS.index(self.level)

    @property
    def name(self):
        return self.__name(self._name)

    @name.setter
    def name(self, value: str):
        self._name = str(value)

    def __name(self, name) -> str:
        if self.color:
            return style(str(name), **self.color.get('name', {}))

        return str(name)

    def __print(self, level: str, message: str, err: bool = True, name: Optional[str] = None):
        if self.color:
            message = style(message, **self.color.get('message', {}))

        if self._stream:
            echo(
                str(self._format.format(
                    **{'level': level, 'name': name, 'message': message}
                )), err=err
            )

        if self._file:
            echo(
                str(self._format_file.format(
                    **{'time': time.time(), 'level': level, 'name': name, 'message': message}
                )), file=open(self._file, 'a+'), color=self._file_force_color
            )

    def debug(self, message: str, name: Optional[str] = None):
        if self.level_index <= 0:
            self.__print(
                style('debug', **self.color.get('debug', {})),
                style(str(message), italic=True),
                name=self.__name(name) if name else self.name
            )

    def info(self, message: str, name: Optional[str] = None):
        if self.level_index <= 1:
            self.__print(
                style('info', **self.color.get('info', {})),
                str(message),
                name=self.__name(name) if name else self.name
            )

    def warning(self, message: str, name: Optional[str] = None):
        if self.level_index <= 2:
            self.__print(
                style('warning', **self.color.get('warning', {})),
                str(message),
                name=self.__name(name) if name else self.name
            )

    def error(self, message: str, name: Optional[str] = None):
        if self.level_index <= 3:
            self.__print(
                style('error', **self.color.get('error', {})),
                str(message),
                name=self.__name(name) if name else self.name
            )

    def critical(self, message: str, name: Optional[str] = None):
        if self.level_index <= 4:
            self.__print(
                style('critical', **self.color.get('critical', {})),
                str(message),
                name=self.__name(name) if name else self.name
            )


CL = ClickLogger
