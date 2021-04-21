#!/usr/bin/env python

from nmpv import Player, StreamRoute

p = Player('pc')
s = StreamRoute('test', 'pc')

p.new(ytdl=True)
filename = 'music/Harris & Ford x Neptunica - Bye Bye (Official Video 4K)-hicFkYsX8rY.mkv'
s.new(filename)
s.start()

for _id in s.routes:
    p.play(s.routes[_id]['url'])
