#!/usr/bin/env python

import os

from kwking_helper import rq

from client import Player

file = os.path.expanduser('~/test.webm')
host = 'pc'

player = Player(host)

if not player.playlist.cache:
    player.new(ytdl=True)

stream = player.stream(file)
stream.start()

if not player.playlist.cache:
    print(f"play {stream.url!r} on {host!r}")
    player.play(stream.url)
else:
    print(f"append {stream.url!r} to playlist on {host!r}")
    player.playlist.append(stream.url)

print(str(player.playlist))

stream.join()
del stream
