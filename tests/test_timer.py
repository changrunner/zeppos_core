import unittest
from zeppos_core.timer import Timer
from testfixtures import log_capture

class TestTheProjectMethods(unittest.TestCase):
    @log_capture()
    def test_start_stop_test_methods(self, capture):
        timer = Timer()
        timer.start_timer()
        timer.pause(time_in_seconds=2)
        timer.stop_timer()

        self.assertEqual(timer.time_elapsed_in_seconds, 2)
        capture.check(
                ('zeppos_logging', 'DEBUG', 'Sleep for [2] seconds'),
        )


if __name__ == '__main__':
    unittest.main()
