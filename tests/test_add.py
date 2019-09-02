"""Example unittest source: Hubertz, J. Softwaretests mit Python 3.1.1 - 3.1.5 S.58-62

Examples for unittest:
3.1.1 Testfall . . . . . . . . . . . . . . . . . . . . . . . . .58
3.1.2 Testvorrichtung, test fixture . . . . . . . . . . . . . . 59
3.1.3 Testgruppe . . . . . . . . . . . . . . . . . . . . . . .  60
3.1.4 Teststarter . . . . . . . . . . . . . . . . . . . . . . . 60
3.1.5 Teststarter im Python-Modul . . . . . . . . . . . . . . . 61

Author: Uwe Schweinsberg, Bochum
License: GNU GPL v 2
Date: 2. 9. 2019

classes: MyFirstTest(unittest.TestCase)
functions: test_true(self)
"""
import unittest
from add import demo_add


class TestDemoAdd(unittest.TestCase):

    def test_calculations_add_ok(self):
        result = demo_add(3, 5)
        expexted = 8
        self.assertEqual(expexted, result)
