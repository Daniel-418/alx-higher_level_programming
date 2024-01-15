#!/usr/bin/python3
"""Tests a file"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test class for the 6-max_integer.py class
    """
    def test_max_integer(self):
        """Tests for general utility of the function"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([-2, -1, 0, 1, 2]), 2)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)

    def test_module_docstring(self):
        """Test if the module docstring exists"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 5)

    def test_function_docstring(self):
        """  
        Checks for the function docstring
        """
        f = max_integer.__doc__
        self.assertTrue(len(f) > 5)

    def test_values(self):
        """Test for unusual values"""
        self.assertIsNone(max_integer())
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer([1, 2, "Hello", 4, 5])

if __name__ == "__main__":
    unittest.main()
