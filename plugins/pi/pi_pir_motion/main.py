
import socket
import sys
import time

from multiprocessing import Process

from helper.config import c
from helper.logging import CL

from helper.thread import threaded2, ThreadData


HOSTNAME = socket.gethostname()

PIN = c.pi_pir_motion.getint(HOSTNAME, 'gpio')
TIMEOUT = c.pi_pir_motion.getfloat(HOSTNAME, 'timeout', fallback=None)
REUSE = c.pi_pir_motion.getfloat(HOSTNAME, 'reuse', fallback=None)
STEP = c.pi_pir_motion.getfloat(HOSTNAME, 'step', fallback=0.25)


class Timeout(Exception):
    pass


class Motion(Process):
    P: Process = Process()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.daemon = True

        self.timeout: float = 0

        self.logger = CL(
            c.main.get('plugin@pi_pir_motion', 'log_level'),
            'PI_PIR_MOTION: Motion',
            _file=c.main.get('plugin@pi_pir_motion', 'log_file', fallback=None)
        )

    def start(self):
        Motion.P = self
        super().start()

    def run(self):
        import threading

        try:
            import pigpio
        except Exception as ex:
            self.logger.critical(f"{ex!r}")
            sys.exit(1)

        self.logger.debug(f"Process Running! {PIN=}")

        pi = pigpio.pi()

        reuse = time.time()
        _thread = ThreadData(
            threading.Thread()
        )
        while True:
            if pi.read(PIN):
                self.logger.debug(f"[{time.time()}] Motion detected")

                if TIMEOUT is not None:
                    self.timeout = time.time() + TIMEOUT

                if REUSE is not None:
                    if time.time() > reuse:
                        if (REUSE == 0) and not _thread.thread.is_alive():
                            # run 'onmotion' command
                            self.logger.info(
                                (
                                    f"[{time.time()}] onmotion:\n"
                                    f"{c.pi_pir_motion.get(HOSTNAME, 'onmotion')}"
                                )
                            )
                            # start timeout method
                            if TIMEOUT is not None and not _thread.thread.is_alive():
                                _thread = self.wait_for_timeout()

                            reuse = time.time() + REUSE
                else:
                    # run 'onmotion' command
                    self.logger.info(
                        (
                            f"[{time.time()}] onmotion:\n"
                            f"{c.pi_pir_motion.get(HOSTNAME, 'onmotion')}"
                        )
                    )
                    # start timeout method
                    if TIMEOUT is not None and not _thread.thread.is_alive():
                        _thread = self.wait_for_timeout()
            else:
                time.sleep(STEP)
                continue

            time.sleep(5)

    @threaded2(daemon=True)
    def wait_for_timeout(self):
        self.logger.debug("waiting for timeout [thread START]")

        try:
            while (timeout := self.timeout - time.time()):
                if timeout > 0:
                    time.sleep(timeout)
                else:
                    raise Timeout()
        except Timeout:
            self.logger.debug("timeout reached, run 'ontimeout' command")
            self.logger.info(
                (
                    f"[{time.time()}] ontimeout:\n"
                    f"{c.pi_pir_motion.get(HOSTNAME, 'ontimeout', fallback=None)}"
                )
            )

        self.logger.debug("waiting for timeout [thread END]")
