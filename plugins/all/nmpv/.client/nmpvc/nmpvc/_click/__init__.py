
from dataclasses import dataclass, field
from typing import Optional

from kwking_helper.logging import CL  # type: ignore
from kwking_helper.thread import ThreadData  # type: ignore

from nmpv_client.base import MPV


@dataclass
class _PL:
    mpv: MPV = None  # type: ignore
    td: list[list[tuple[str, ThreadData]]] = field(default_factory=list)


@dataclass
class _SMB:
    server: str
    share: str
    username: str
    password: str
    port: int = 139
    path: str = '/'
    files: list[str] = field(default_factory=list)

    def url(self, file):
        return "smb://{}:{}@{}/{}/{}".format(
            self.username, self.password,
            self.server, self.share,
            f"{self.path}/{file.lstrip('/')}".lstrip('/')
        )

    def add(self, file: str):
        self.files.append(str(file))


@dataclass
class _Cache:
    pl = _PL()
    smb: Optional[_SMB] = None
    help = None
    _cl = CL('info', __name__)

    @property
    def logger(self):
        return self._cl


Cache = _Cache()
