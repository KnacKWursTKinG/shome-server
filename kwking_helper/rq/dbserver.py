
from typing import Union, Optional

import requests

from .base import RQBase, RQError


class DBServerError(Exception):
    pass


class DBServer(RQBase):
    def __init__(self, auth: Union[str, bytes],
                 host: str = 'localhost', port: int = 50860):

        super().__init__(host, port)

        if isinstance(auth, bytes):
            self.auth2(auth)
        elif isinstance(auth, str):
            if ':' not in auth:
                raise DBServerError("missing ':' for auth [format: <username>: <password>]")
            self.auth(*auth.split(':'))
        else:
            raise DBServerError(f"auth should be {type(bytes())!r} or {type(str())!r} not {type(auth)!r}")

    def _create_path(self, group: Optional[str], label: Optional[str]) -> str:
        if label and not group:
            raise DBServerError("group needed for label")

        return f"{((group + '/') if group else '')}{label if (group and label) else ''}"

    def get(self, group: str = None, label: str = None) -> requests.Response:
        return requests.get(
            f"{self.url}/db/{self._create_path(group, label)}",
            headers=self.headers,
            timeout=self.timeout
        )

    def post(self, group: str, label: str, data: bytes,
             _auto_put: bool = False) -> requests.Response:

        assert isinstance(data, bytes), f"data have to be {type(data)!r}"

        headers = {**self.headers, **{'Content-Type': 'data/bytes'}}

        r = requests.post(
            f"{self.url}/db/{self._create_path(group, label)}",
            data=data,
            headers=headers,
            timeout=self.timeout
        )

        if not r and _auto_put:
            if 'use put' in r.text.lower():
                r = self.put(group, label, data)

        return r

    def put(self, group: str, label: str, data: bytes,
            _auto_post: bool = False) -> requests.Response:

        assert isinstance(data, bytes), f"data have to be {type(data)!r}"

        headers = {**self.headers, **{'Content-Type': 'data/bytes'}}

        r = requests.put(
            f"{self.url}/db/{self._create_path(group, label)}",
            data=data,
            headers=headers,
            timeout=self.timeout
        )

        if not r and _auto_post:
            if 'use post' in r.text.lower():
                r = self.post(group, label, data)

        return r

    def delete(self, group: str, label: str = None):
        return requests.delete(
            f"{self.url}/db/{self._create_path(group, label)}",
            headers=self.headers
        )
