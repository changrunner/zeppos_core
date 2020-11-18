import unittest
from zeppos_core.timer import Timer
from testfixtures import LogCapture
from zeppos_logging.app_logger import AppLogger

class TestTheProjectMethods(unittest.TestCase):
    def test_start_stop_test_methods(self):
        AppLogger.configure_and_get_logger('start_stop_test')
        AppLogger.set_debug_level()

        with LogCapture() as lc:
            timer = Timer()
            timer.start_timer()
            timer.pause(time_in_seconds=2)
            timer.stop_timer()

            self.assertEqual(timer.time_elapsed_in_seconds, 2)
            lc.check_present(
                ('start_stop_test', 'DEBUG', 'Sleep for [2] seconds'),
            )


if __name__ == '__main__':
    unittest.main()
