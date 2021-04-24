#!/usr/bin/env python

import readline
import re
import os

from threading import Thread, Lock

from kwking_helper.thread import threaded

from nmpvc.ctrl import Control
from nmpvc.stream import Stream

HOSTS = ['pc']
FILE = os.path.expanduser('~/test.webm')

seek_regex = re.compile(r"(?P<pre>[+-]?)(?P<time>([0-9\.]*))$")

ctrl = list()
for host in HOSTS: ctrl.append(Control(host))

for _ in ctrl: _.new(ytdl=True, pause=True)


@threaded(True)
def print_info():
    tlock = Lock()

    @threaded(True)
    def _print(_ctrl):
        duration = _ctrl.duration
        time_pos = _ctrl.time_pos

        with tlock:
            print(f"[{_ctrl.host}] {duration=}, {time_pos=}")

    for _ in ctrl:
        _print(_)

try:
    with Stream(FILE, HOSTS, log_level='debug') as stream:
        for _ in ctrl: _.play(stream)

        while (_input := input("Seek or Quit: \n")):
            if _input in ['quit', 'q']:
                break

            if _input in ['play', 'pause']:
                for _ in ctrl: _.pause = bool(_input == 'pause')
                continue

            match = re.match(seek_regex, _input)

            if match:
                _t = list()
                for _ in ctrl: _t.append(_.seek(f"{match.group('pre')}{match.group('time')}"))
                for _ in _t: _.join()

            print_info()

finally:
    _t = list()
    for _ in ctrl: _t.append(_.quit())
    for _ in _t: _.join()
