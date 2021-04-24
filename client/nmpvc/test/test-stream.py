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

CTRL = list()

for host in HOSTS:
    ctrl = Control(host)
    ctrl.new(ytdl=True, pause=True)
    CTRL.append(ctrl)


@threaded(True)
def print_info():
    tlock = Lock()

    @threaded(True)
    def _print(ctrl):
        duration = ctrl.duration
        time_pos = ctrl.time_pos

        with tlock:
            print(f"[{ctrl.host}] {duration=}, {time_pos=}")

    threads = list()
    for ctrl in CTRL:
        threads.append(_print(ctrl))

    for _ in threads:
        _.join()


@threaded(True)
def pause(state):
    @threaded(True)
    def _thread(ctrl):
        ctrl.pause = state

    threads = list()
    for ctrl in CTRL:
        _thread(ctrl)

    for _ in threads:
        _.join()


@threaded(True)
def seek(*args, **kwargs):
    @threaded(True)
    def _thread(ctrl):
        ctrl.seek(*args, **kwargs)

    threads = list()
    for ctrl in CTRL:
        _thread(ctrl)

    for _ in threads:
        _.join()


try:
    with Stream(FILE, HOSTS, log_level='debug') as stream:
        for ctrl in CTRL:
            Thread(target=ctrl.play, args=(stream,)).start()

        while (_input := input("Seek or Quit: \n")):
            if _input in ['quit', 'q']:
                break

            if _input in ['play', 'pause']:
                pause(bool(_input == 'pause'))
                continue

            match = re.match(seek_regex, _input)

            if match:
                seek(f"{match.group('pre')}{match.group('time')}")

            print_info()

finally:
    for ctrl in CTRL:
        Thread(target=ctrl.quit, daemon=False).start()
