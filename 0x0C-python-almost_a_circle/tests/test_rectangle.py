#!/usr/bin/python3
"""Defines TestCases for Rectangle Class Module"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleValidation(unittest.TestCase):

    def test_first_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_second_validation(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10

    def test_third_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}

    def test_fourth_validation(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)


class TestRectangleArea(unittest.TestCase):

    def test_first_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(6, r1.area())

    def test_second_area(self):
        r2 = Rectangle(2, 10)
        self.assertEqual(20, r2.area())

    def test_third_area(self):
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(56, r3.area())


class TestGetterAndSetter(unittest.TestCase):

    def test_width_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)


if __name__ == '__main__':
    unittest.main()
