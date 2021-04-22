""" Some basic class for sending nmpv commands """

import socket
import pickle

import requests

from kwking_helper import rq


__all__ = ['CTRL']


class CTRL:
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
        return self.run('pause')

    @pause.setter
    def pause(self, state: bool):
        self.run('pause', bool(state))
