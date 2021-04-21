#!/usr/bin/env python

import os

from nmpv import Player

p = Player('pc')
file = os.path.expanduser('~/test.webm')

p.new(ytdl=True)
p.stream(file)
