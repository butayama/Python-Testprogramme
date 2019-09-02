"""Example unittest source: Hubertz, J. Softwaretests mit Python 3. S.58

Examples for unittest: Erster Testlauf

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