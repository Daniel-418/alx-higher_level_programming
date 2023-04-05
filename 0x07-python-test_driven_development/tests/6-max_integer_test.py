#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.Testcase):
    def test_max_integer(self):
        self.assertEqual(5, max([1, 2, 3, 4, 5, 3, 2, 1, 0]))

    def test_None(self):
        self.assertIsNone(max([]))

    def test_Negative(self):
        self.assertEqual(-1, max([-23, -4, -6, -7, -9, -1]))

if __name__ == '__main__':
    unittest.main()
