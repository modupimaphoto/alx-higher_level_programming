#!/usr/bin/python3
"""Defines TestCases for Base Class Module"""
import unittest
from models.base import Base


class TestBaseModule(unittest.TestCase):

    def test_initialization(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(1, base1.id)
        self.assertEqual(2, base2.id)

    def test_id(self):
        base = Base(100)
        self.assertEqual(100, base.id)


if __name__ == '__main__':
    unittest.main()
