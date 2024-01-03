#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test case with a list of positive integers
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

        # Test case with a list of negative integers
        self.assertEqual(max_integer([-5, -4, -3, -2, -1]), -1)

        # Test case with a list of mixed positive and negative integers
        self.assertEqual(max_integer([-2, 0, 3, -5, 2]), 3)

        # Test case with an empty list
        self.assertIsNone(max_integer([]))

if __name__ == '__main__':
    unittest.main()
