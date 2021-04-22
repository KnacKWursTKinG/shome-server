
import os
import time
import socket
import unittest

import requests

from kwking_helper import rq


HOST = 'pc'
PORT = int(50870)


class Test001CTRL(unittest.TestCase):
    def test_001_init(self):
        from nmpv_ctrl.ctrl import CTRL

        ctrl = CTRL(HOST, str(PORT))

        assert ctrl.host == '127.0.1.1', f"{ctrl.host=}"
        assert CTRL(ctrl.host).host == '127.0.1.1', f"{ctrl.host=}"
        assert isinstance(ctrl.port, int), f"{ctrl.port=}"
        assert ctrl.name == 'nmpv', f"{ctrl.name=}"

        self.assertRaises(socket.gaierror, CTRL, 'unknown-host')

        assert ctrl.url == f"http://{ctrl.host}:{ctrl.port}/api/nmpv/player", f"{ctrl.url=}"

    def test_002_run(self):
        from nmpv_ctrl.ctrl import CTRL

        ctrl = CTRL(HOST, str(PORT))

        try:
            _return = ctrl.run('new', ytdl=True)
            assert _return == None, f"{_return=}"

        except rq.RQError as r:
            print(f"\nrq.RQError: {r!r}")

        except requests.exceptions.ConnectionError:
            print("\nServer Offline")


class Test002Playlist(unittest.TestCase):
    def test_001_init(self):
        from nmpv_ctrl.playlist import Playlist

        print()
        pl = Playlist(HOST, str(PORT), log_level='debug')
        pl.reload()

        assert not pl, f"{pl!s}"

    def test_002_playlist(self):
        from nmpv_ctrl.playlist import Playlist, _PlaylistItem

        print()
        pl = Playlist(HOST, str(PORT), log_level='debug')
        pl.run('play', 'http://test.url')

        assert pl, f"{pl!s}"

        assert len(pl) == 1, f"{pl!s}"
        assert 1 in pl, f"{pl!s}"
        assert "http://test.url" in pl, f"{pl!s}"
        assert isinstance(pl[0], _PlaylistItem), f"{type(pl[0])!r}"

        try:
            assert not pl[1], f"position '{1}' found: {pl[1]}"
        except IndexError:
            pass

    def test_003_getters(self):
        from nmpv_ctrl.playlist import Playlist, _PlaylistItem

        print()
        pl = Playlist(HOST, str(PORT), log_level='debug')

        assert pl.pos == 0, f"{pl.pos!r}"

        pl.run('new', ytdl=True)
        pl.run('playlist_append', os.path.abspath(os.path.expanduser('~/test.webm')))
        el = pl[0]

        assert pl.pos == -1, f"{pl.pos!r}"
        assert pl.index(el.id) == 0, f"{pl.index(el.id)!r}"
        assert pl.index(el) == 0, f"{pl.index(el)!r}"

    def test_004_setters(self):
        from nmpv_ctrl.playlist import Playlist, _PlaylistItem

        print()
        pl = Playlist(HOST, str(PORT), log_level='debug')
        pl.reload()

        pl.pause = True

        assert pl.pos == -1, f"{pl.pos!r}"

        pl.pos = 0

        assert pl.pos == 0, f"{pl.pos!r}"
        assert pl.pause is True, f"{pl.pause!r}"

        pl.pause = False

        assert pl.pause is False, f"{pl.pause!r}"
        assert pl[pl.index(1)].playing is True, f"{pl[pl.index(1)].playing!r}"
        assert pl[pl.index(1)].current is True, f"{pl[pl.index(1)].current!r}"

        # quit
        #pl.run('new', ytdl=True)
        pl.run('quit')

        assert not pl, f"{pl!s}"


if __name__ == "__main__":
    unittest.main()
