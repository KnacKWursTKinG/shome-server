
from __future__ import annotations

import threading

from dataclasses import dataclass
from typing import Any, Optional, Callable


@dataclass
class ThreadData:
    thread: threading.Thread = threading.Thread()
    _return: Optional[Any] = None
    _error: Optional[Exception] = None

    @property
    def ret(self):
        return self._return

    @property
    def err(self):
        return self._error

    def join(self, timeout: Optional[float] = None) -> Any:
        self.thread.join(timeout)

        if self.err:
            raise self.err

        return self.ret


def threaded(daemon: bool = True):
    def decorate(func):
        def call(*args, **kwargs):
            def thread_wrap(self):
                try:
                    self._return = func(*args, **kwargs)
                except Exception as ex:
                    self._error = ex

            tdata = ThreadData()

            tdata.thread = threading.Thread(
                target=thread_wrap,
                args=(tdata,),
                daemon=daemon
            )

            tdata.thread.start()

            return tdata

        return call

    return decorate


# @todo: add name (Thread().name)
def threaded2(daemon: bool = True, on_success: Optional[Callable] = None, on_error: Optional[Callable] = None):
    def decorate(func):
        def call(*args, **kwargs):
            @threaded2(daemon)
            def on_handler(t: ThreadData):
                t.thread.join()

                if on_success and not t.err:
                    on_success(t, t.ret)

                elif on_error and t.err:
                    on_error(t, t.err)

            def thread_wrap(self):
                try:
                    self._return = func(*args, **kwargs)
                except Exception as ex:
                    self._error = ex

            tdata = ThreadData()

            tdata.thread = threading.Thread(
                target=thread_wrap,
                args=(tdata,),
                daemon=daemon
            )

            tdata.thread.start()

            if on_success or on_error:
                on_handler(tdata)

            return tdata

        return call

    return decorate
