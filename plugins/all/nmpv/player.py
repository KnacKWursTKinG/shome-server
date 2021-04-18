
import pickle
import socket

from typing import Union, Optional, Any
from flask import make_response

import mpv

from kwking_helper import c, thread


PLAYER: mpv.MPV = None

DEFAULT_PLAYER_ARGS = c.mpv.get(
    socket.gethostname(), 'player_args',
    fallback=None
) or dict()


@thread(
    daemon=True,
    log_level=c.main.get('plugin@nmpv', 'log_level', fallback='warning')
)
def player(data: bytes):
    global PLAYER

    attr: Union[str, Any]
    args: Optional[tuple[Any]]
    kwargs: Optional[dict[str, Any]]

    _return: Any = None
    default_player_args = DEFAULT_PLAYER_ARGS

    attr, args, kwargs = pickle.loads(data)

    if attr == 'new':
        # quit PLAYER if not None and del + set to None
        if PLAYER is not None:
            PLAYER.quit(0)
            PLAYER.terminate()
            del PLAYER
            PLAYER = None

        # get player args
        if isinstance(kwargs, dict) and kwargs:
            default_player_args = {
                **default_player_args,
                **kwargs
            }

    if PLAYER is None:
        PLAYER = mpv.MPV(**default_player_args)

    # TODO: ...
    ...

    return make_response(
        pickle.dumps(_return), 200
    )
