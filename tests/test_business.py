import unittest
from zeppos_core.business import Business
from freezegun import freeze_time
from datetime import datetime


class TestTheProjectMethods(unittest.TestCase):
    @freeze_time('2018-06-29 10:15:27.243860')
    def test_are_we_during_business_hours_true_method(self):
        self.assertEqual(True, Business.are_we_during_business_hours("6", "18.5"))

    @freeze_time('2018-06-29 22:15:27.243860')
    def test_are_we_during_business_hours_true_method(self):
        self.assertEqual(False, Business.are_we_during_business_hours("6", "18.5"))


if __name__ == '__main__':
    unittest.main()
