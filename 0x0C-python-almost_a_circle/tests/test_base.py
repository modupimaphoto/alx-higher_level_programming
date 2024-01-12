#!/usr/bin/python3
"""Defines TestCases for Base Class Module"""
import unittest
from models.base import Base


class TestBaseModule(unittest.TestCase):
    
    def test_nb_objects(self):
        if __name__ == "__main__":
            b1 = Base()
            self.assertEqual(1, b1.id)
            b2 = Base()
            self.assertEqual(2, b2.id)
            b3 = Base()
            self.assertEqual(3, b3.id)
            b4 = Base(12)
            self.assertEqual(12, b4.id)
            b5 = Base()
            self.assertEqual(4, b5.id)

if __name__ == '__main__':
    unittest.main()
