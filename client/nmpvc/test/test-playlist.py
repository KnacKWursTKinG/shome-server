#!/usr/bin/env python

import os
import time

from nmpvc.playlist import Playlist

from kwking_helper import rq

test_file = os.path.expanduser('~/test.webm')


class Playlist(Playlist):
    def reload(self):
        # NOTE: sometimes the client is faster than the server
        time.sleep(.1)
        self.__refresh__()


pl = Playlist('pc', log_level='debug')
pl.run('new', ytdl=True)
pl.append(test_file)
pl.append(test_file)
pl.reload()

# check playlist
assert len(pl) == 2, str(pl)
assert pl[0].filename == test_file, str(pl)
assert pl[1].filename == test_file, str(pl)
assert pl[0].current is True, str(pl)
assert pl[1].current is False, str(pl)
assert pl[0].playing is False, str(pl)
assert pl[1].playing is False, str(pl)
assert pl.pos == 0, pl.pos

# play first in pl
pl.pos = 0
pl.reload()
assert pl[0].current is True, str(pl)
assert pl[1].current is False, str(pl)
assert pl[0].playing is True, str(pl)
assert pl[1].playing is False, str(pl)

# play second in pl
pl.pos = 1
pl.reload()
assert pl[0].current is False, str(pl)
assert pl[1].current is True, str(pl)
assert pl[0].playing is False, str(pl)
assert pl[1].playing is True, str(pl)

# pause
pl.pause = True
pl.reload()
assert pl.pause is True
assert pl[0].current is False, str(pl)
assert pl[1].current is True, str(pl)
assert pl[0].playing is False, str(pl)
assert pl[1].playing is True, str(pl)


pl.time_pos = pl.duration / 2
assert pl.time_pos == pl.duration / 2, pl.time_pos

pl.pause = False
assert pl.time_pos >= (pl.duration / 2), f"{pl.time_pos=}, {pl.duration / 2}"

try:
    pl.remove(-1)
except rq.RQError as ex:
    if ex.response.status_code == 500:
        print("Server Error")

    else:
        print(f"{ex.response!r}, {ex.response.text}")

# quit
import readline
import re
seek_regex = re.compile(f"(?P<pre>[+-]?)(?P<time>([0-9]*))$")
while (_input := input("Seek or Quit: ")):
    if _input in ['quit', 'q']:
        break

    match = re.match(seek_regex, _input)

    if match:
        pl.seek(f"{match.group('pre')}{match.group('time')}")

    print(f"{pl.duration=}, {pl.time_pos=}")

pl.quit()
pl.reload()
assert not pl
