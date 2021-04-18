
import pickle
import socket

from typing import Union, Optional, Any
from flask import make_response

import mpv

from kwking_helper import c, thread


@thread(
    daemon=True,
    log_level=c.main.get('plugin@mpv', 'log_level', fallback='warning')
)
def player(data: bytes):
    global Player

    attr: Union[str, Any]
    args: Optional[tuple[Any]]
    kwargs: Optional[dict[str, Any]]

    defaults = c.mpv.get(
        socket.gethostname(), 'player_args',
        fallback=None
    ) or dict()
    _return: Any = None

    attr, args, kwargs = pickle.loads(data)

    # TODO: ...
    ...

    return make_response(
        pickle.dumps(_return), 200
    )
