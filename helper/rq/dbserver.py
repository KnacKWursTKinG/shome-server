
import requests

from .base import RQBase


class DBServerError(Exception):
    pass


class DBServer(RQBase):
    def __init__(self, host: str = 'localhost', port: int = 50860):
        super().__init__(host, port)

    def get(self, path: str, **params) -> requests.Response:
        return requests.get(
            f"{self.url}/{path.lstrip('/')}",
            params=params,
            headers=self.headers,
            timeout=self.timeout
        )

    def post(self, path, data: str, **params) -> requests.Response:

        assert isinstance(data, str), "data have to be a json string"

        headers = {**self.headers, **{'Content-Type': 'application/json'}}

        r = requests.post(
            f"{self.url}/{path.lstrip('/')}",
            data=data,
            params=params,
            headers=headers,
            timeout=self.timeout
        )

        return r

    def delete(self, path: str, **params):
        return requests.delete(
            f"{self.url}/{path.lstrip('/')}",
            params=params,
            headers=self.headers
        )
