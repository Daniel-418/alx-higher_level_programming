#!/usr/bin/python3
"""Test module for the base class project"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test class for the Base model class"""

    def test_private_class_attribute(self):
        """Tests if the class has a private class attribute"""
        base = Base()
        self.assertTrue(hasattr(base, '_Base__nb_objects'))

    def test_id(self):
        """Tests that the id is correct"""
        base1 = Base()
        base2 = Base(19)
        base3 = Base()
        base4 = Base()
        base5 = Base()
        base6 = Base()

        self.assertTrue(hasattr(base2, 'id'))
        self.assertEqual(base2.id, 19)
        self.assertEqual(base3.id, base1.id + 1)
        self.assertEqual(base4.id, base3.id + 1)
        self.assertEqual(base5.id, base4.id + 1)

    def test_public_id(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(b.id, 15)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_class_docstring(self):
        """Tests if the class has a docstring"""
        self.assertIsNotNone(Base.__doc__, "Base should have a docstring")

if __name__ == "__main__":
    unittest.main()
