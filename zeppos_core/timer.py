from zeppos_logging.app_logger import AppLogger
import time
from datetime import datetime

class Timer:
    def __init__(self):
        self._start_time = datetime.now()
        self._end_time = self._start_time

    def start_timer(self):
        self._start_time = datetime.now()

    def stop_timer(self):
        self._end_time = datetime.now()

    def pause(self, time_in_seconds):
        AppLogger.logger.debug(f'Sleep for [{time_in_seconds}] seconds')
        time.sleep(time_in_seconds)

    @property
    def time_elapsed_in_seconds(self):
        return int((self._end_time - self._start_time).total_seconds())