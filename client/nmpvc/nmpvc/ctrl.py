""" Some basic class for sending nmpv commands """

import socket
import pickle

from typing import Any, Union, Optional

import requests

from kwking_helper import rq
from kwking_helper.thread import threaded, ThreadData

from nmpvc.stream import Stream


__all__ = ['Control']


class Control:
    name: str = 'nmpv'

    def __init__(self, host: str, port: int = 50870):
        """ Basic Control Methods

        Args:
            host: shomeserver hostname to control
            port: shomeserver port [default: 50870]

        Raises:
            socket.gaierror: if host not found
        """
        self.host = socket.gethostbyname(host)
        self.port = int(port)

    @property
    def url(self) -> str:
        return f"http://{self.host}:{self.port}/api/{self.name}/player"

    @threaded(True)
    def run(self, attr: str, *args, **kwargs):
        """ Send nmpv package

        Example:
            >>> self.run('new', ytdl=True) # create a new player instance
            >>> self.run('play', 'http://url')  # play video
            >>> self.run('duration')  # get duration from video
            >>> self.run('pause', True)  # set pause

        Args:
            attr: nmpv attribute to run based on args and kwargs

        Raises:
            rq.RQError: response: if not response
            requests.exceptions.ConnectionError: server not reachable
        """
        response = requests.post(
            self.url,
            pickle.dumps(
                (str(attr), args, kwargs)
            ),
            headers={
                'Content-Type': 'data/bytes'
            }
        )

        if not response:
            raise rq.RQError(response)

        return pickle.loads(response.content)

    @property
    def pause(self) -> bool:
        return self.run('pause').join()

    @pause.setter
    def pause(self, state: bool) -> ThreadData:
        return self.run('pause', bool(state))

    @property
    def duration(self) -> Optional[Union[float]]:
        return self.run('duration').join()

    @duration.setter
    def duration(self):
        pass

    @property
    def time_pos(self) -> Optional[Union[int, float]]:
        return self.run('time_pos').join()

    @time_pos.setter
    def time_pos(self, pos: Union[int, float]) -> ThreadData:
        return self.run('time_pos', float(pos))

    @property
    def time_remaining(self) -> Optional[Union[int, float]]:
        return self.run('time_remaining').join()

    @time_remaining.setter
    def time_remaining(self):
        pass

    def new(self, **player_args) -> ThreadData:
        """ crate a new MPV Player """
        return self.run('new', **player_args)

    def play(self, file: Union[str, Stream]) -> ThreadData:
        """ Play a file or url """
        if isinstance(file, Stream):
            _file = file.url

            if not file.is_alive():
                file.start()
        else:
            _file = file

        return self.run('play', str(_file))

    def seek(self, amount: Union[str, int, float], reference='relative',
             precision='default-precise') -> ThreadData:

        return self.run('seek', amount, **dict(reference=reference, precision=precision))

    def quit(self) -> ThreadData:
        return self.run('quit')
