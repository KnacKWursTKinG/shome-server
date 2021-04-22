#!/usr/bin/env python

import os

from pprint import pprint

from kwking_helper import rq

from client import Player

file = os.path.expanduser('~/test.webm')
host = 'pc'

player = Player(host)

player.new(ytdl=True)

stream = player.stream(file)
stream.start()

if not player.playlist:
    print("play {file!r} on {host!r}")
    player.play(stream.url)
else:
    print("append {file!r} to playlist on {host!r}")
    player.playlist.append(stream.url)

stream.join()
del stream

pprint(player.playlist)
