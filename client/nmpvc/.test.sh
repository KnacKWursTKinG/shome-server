#!/usr/bin/env zsh

python nmpvc --debug \
  smb \
    -c rpi-server MyNAS alarm nincompoop \
    --path '/videos/music' \
  search \
    --sort 'write' \
    -m 1 \
    '.*' \
  append \
    --server localhost \
  on-success \
    --echo \
    --exit \
  pl list
