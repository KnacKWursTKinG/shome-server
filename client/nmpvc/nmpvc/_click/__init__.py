
import threading

from dataclasses import dataclass, field
from typing import Optional

from kwking_helper.logging import CL


TL = threading.Lock()


@dataclass
class _PL:
    url: list[str] = field(default_factory=list)

    def add(self, url: str):
        with TL:
            self.url.append(str(url))


@dataclass
class _SMB:
    server: str
    share: str
    username: str
    password: str
    port: int = 139
    path: str = '/'

    def url(self, file):
        return "smb://{}:{}@{}/{}/{}".format(
            self.username, self.password,
            self.server, self.share,
            f"{self.path}/{file.lstrip('/')}".lstrip('/')
        )


@dataclass
class _Cache:
    pl = _PL()
    smb: Optional[_SMB] = None
    _cl = CL('warning', __name__)

    @property
    def logger(self):
        return self._cl


Cache = _Cache()
