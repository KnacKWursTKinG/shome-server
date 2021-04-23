#!/usr/bin/env python

import os

from nmpvc.ctrl import Control
from nmpvc.stream import Stream

HOST = 'pc'
FILE = os.path.expanduser('~/test.webm')

ctrl = Control(HOST)
ctrl.new(ytdl=True, pause=True)

stream = Stream(HOST, FILE, 'debug')

ctrl.play(stream)

import readline
import re
seek_regex = re.compile(f"(?P<pre>[+-]?)(?P<time>([0-9]*))$")
while (_input := input("Seek or Quit: ")):
    if _input in ['quit', 'q']:
        break

    match = re.match(seek_regex, _input)

    if match:
        ctrl.seek(f"{match.group('pre')}{match.group('time')}")

    print(f"{ctrl.duration=}, {ctrl.time_pos=}")

ctrl.quit()
