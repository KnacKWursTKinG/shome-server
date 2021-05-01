
import time


class SyncError(Exception):
    pass


def sync(timestamp: float) -> float:
    time_to_wait = timestamp - time.time()

    if time_to_wait <= 0:
        raise SyncError(time_to_wait)

    time.sleep(time_to_wait)

    return time.time()
