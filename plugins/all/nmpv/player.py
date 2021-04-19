
import pickle
import socket
import types
import json

from typing import Union, Optional, Any

import mpv

from kwking_helper import c, thread, ClickLogger


logger = ClickLogger(
    c.main.get('plugin@nmpv', 'log_level'),
    name='MPV: player',
    _file=c.main.get('plugin@nmpv', 'log_file', fallback=None)
)

PLAYER: mpv.MPV = None

try:
    DEFAULT_PLAYER_ARGS = json.loads(
        c.mpv._sections.get(socket.gethostname(), '{}')
    )
except AttributeError:
    logger.warning(f"no mpv configuration found for {socket.gethostname()!r}")
    DEFAULT_PLAYER_ARGS = dict()


@thread(
    daemon=True,
    log_level=c.main.get('plugin@nmpv', 'log_level', fallback='warning')
)
def player(data: bytes):
    global PLAYER

    attr: Union[str, Any]
    args: tuple[Any]
    kwargs: dict[str, Any]

    _return: Any = None
    default_player_args = DEFAULT_PLAYER_ARGS

    attr, args, kwargs = pickle.loads(data)

    if attr == 'new':
        # quit PLAYER if not None and del + set to None
        if PLAYER is not None:
            logger.debug('terminate existing player')
            PLAYER.quit(0)
            PLAYER.terminate()
            del PLAYER
            PLAYER = None

        # get player args
        if isinstance(kwargs, dict) and kwargs:
            logger.debug(f"set custom player args {kwargs=}")
            default_player_args = {
                **default_player_args,
                **kwargs
            }

    if PLAYER is None:
        logger.debug(f"init mpv.MPV({default_player_args=})")
        PLAYER = mpv.MPV(**default_player_args)

    if attr != 'new':
        attr = getattr(PLAYER, attr)
        logger.debug(f"{type(attr)=}")

        if isinstance(attr, types.MethodType):
            logger.debug(f"run {attr=}")
            _return = attr(
                *args, **kwargs
            )

        else:
            logger.debug(f"get {attr=}")
            _return = attr

    logger.debug(f"return: {_return=}")

    return pickle.dumps(_return)
