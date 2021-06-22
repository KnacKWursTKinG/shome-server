
import base64
import socket

from typing import Union

from requests import Response


class RQError(Exception):
    def __init__(self, response: Response):
        super().__init__(f"{response!r}, {response.text}")
        self.response = response


class RQBase:
    def __init__(self, host: str, port: int):
        self.host: str = socket.gethostbyname(host)
        self.port: int = int(port)
        self.url: str = f"http://{self.host}:{self.port}"
        self.timeout: Union[str, float] = 3
        self.headers: dict[str, str] = {}

    def auth(self, username: str, password: str):
        """ Authorization header """
        credentials = base64.b64encode(f"{username}:{password}".encode('utf-8'))
        self.auth2(credentials)

    def auth2(self, credentials: bytes):
        """ base64 encoded string ("<username>:<password>") """
        self.headers['Authorization'] = f"Basic {str(credentials, 'utf-8')}"
