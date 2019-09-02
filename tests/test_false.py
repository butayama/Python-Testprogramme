"""Example unittest source: Hubertz, J. Softwaretests mit Python 3.2.3 S.64

Examples for unittest: Dritter Testlauf

Author: Uwe Schweinsberg, Bochum
License: GNU GPL v 2
Date: 2. 9. 2019

classes: MyFirstTest(unittest.TestCase)
functions: test_true(self)
"""
import unittest

class MyFirstTest(unittest.TestCase):

    def test_true(self):
        self.assertTrue(self)


    def test_false(self):
        assert False