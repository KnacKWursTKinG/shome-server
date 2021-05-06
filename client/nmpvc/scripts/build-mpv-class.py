#!/usr/bin/env python

from __future__ import annotations

import threading
import inspect
import pprint

import mpv

from kwking_helper.thread import threaded2, ThreadData
from kwking_helper.logging import CL


logger = CL(
    'debug', __name__, _file='mympv.log',
    _format="[{level}] {message}",
    _format_file="[{level}] {message}",
    _file_force_color=True
)


class MPV:
    def _run(self, method: str, *args, **kwargs):
        print(f'[_run] {method=}, {args=}, {kwargs=}')

    def _set(self, prop: str, value):
        print(f'[_set] {prop=}, {value=}')

    def _get(self, prop: str):
        print(f'[_get] {prop=}')
        ...

    def new(self, *flags, **player_args):
        ...

    def quit(self):
        self._run('quit')

    def terminate(self):
        self.quit()


class BuildClass:
    Queue: list[BuildClass] = list()
    ThreadLock = threading.Lock()

    def __init__(self, class_obj):
        self.class_obj = class_obj

        self.__thread = None

    def run(self, obj, name):
        attr = getattr(obj, name)

        if isinstance(attr, types.MethodType):
            # @todo: get args and kwargs via inspect module and add to class
            params = inspect.getfullargspec(attr)
            ...

            with BuildClass.ThreadLock:
                if params.varargs and params.varkw:
                    logger.debug(f"[add method] player.{name}({', '.join(list(map(str, params.args)))}, *{params.varargs}, **{params.varkw})")
                elif params.varargs:
                    logger.debug(f"[add method] player.{name}({', '.join(list(map(str, params.args)))}, *{params.varargs})")
                elif params.varkw:
                    logger.debug(f"[add method] player.{name}({', '.join(list(map(str, params.args)))}, **{params.varkw})")
                else:
                    logger.debug(f"[add method] player.{name}({', '.join(list(map(str, params.args)))})")

                if params.kwonlyargs:
                    logger.debug(f"[add method] ... {params.kwonlyargs=}")
                    logger.debug(f"[add method] ... {params.kwonlydefaults=}")

        else:
            with BuildClass.ThreadLock:
                self.class_obj.__setattr__(name, property(
                    lambda self: self._get(name),
                    lambda self, value: self._set(name, value)
                ))

                logger.debug(f"[add property] {name}")
                logger.debug(f"[add property] ... defalut:\n{pprint.pformat(getattr(obj, name))}")

    def start(self, obj, attr):
        if self.__thread is not None:
            logger.critical(f"[{self.__thread.thread.name}] Thread already started!")
            return

        @threaded2(True, on_success, on_error)
        def _run(self, obj, attr):
            self.run(obj, attr)

        self.__thread = _run(self, obj, attr)

    @classmethod
    def wait_for_finish(cls):
        while (_thread := BuildClass.Queue.pop(0) if BuildClass.Queue else None):
            _thread.join()
            del _thread


def on_success(td: ThreadData, ret):
    pass


def on_error(td: ThreadData, err):
    with BuildClass.ThreadLock:
        logger.error(f"[{td.thread.name}] [on_error] {err!r}")


if __name__ == "__main__":
    import types
    import pickle

    with open('mympv.log', 'w') as file:
        pass

    player = mpv.MPV()
    new_player = MPV()

    for _attr in dir(player):
        if _attr[0] == '_':
            continue

        BuildClass(new_player).start(player, _attr)

    BuildClass.wait_for_finish()

    # store MPV class in pickle file
    with open('mpv.pickle', 'wb') as file:
        pickle.dump(MPV, file)
