import sys
import unittest
from datetime import timedelta

from pulsar import reraise


class TestMiscellaneous(unittest.TestCase):

    def test_reraise(self):
        self.assertRaises(RuntimeError, reraise, RuntimeError, RuntimeError())
        try:
            raise RuntimeError('bla')
        except Exception:
            exc_info = sys.exc_info()
        self.assertRaises(RuntimeError, reraise, *exc_info)
