
import time


class SyncError(Exception):
    pass


def sync(timestamp: float) -> float:
    ts = timestamp - time.time()
    print(f"{ts=}, ({timestamp=} - {time.time()=})", flush=True)

    try:
        time.sleep(ts)
    except ValueError as ex:
        raise SyncError(ts) from ex

    return time.time()
