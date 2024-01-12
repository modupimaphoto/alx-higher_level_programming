"""Defines TestCases for Square Module"""
from models.square import Square
import unittest


class TestSquareArea(unittest.TestCase):

    def test_first_area(self):
        s1 = Square(5)
        self.assertEqual(25, s1.area())

    def test_second_area(self):
        s2 = Square(2, 2)
        self.assertEqual(4, s2.area())

    def test_third_area(self):
        s3 = Square(3, 1, 3)
        self.assertEqual(9, s3.area())

    def test_fourth_area(self):
        with self.assertRaises(TypeError):
            s4 = Square(3, '10')

    def test_firth_area(self):
        with self.assertRaises(ValueError):
            s5 = Square(3, -1, 3)


class TestSquareGetterAndSetter(unittest.TestCase):

    def test_first_size_getter(self):
        s1 = Square(5)
        self.assertEqual(5, s1.size)

    def test_second_size_getter(self):
        s2 = Square(5)
        s2.size = 10
        self.assertEqual(10, s2.size)

    def test_first_size__setter(self):

        with self.assertRaises(TypeError):
            s3 = Square(5)
            s3.size = '10'

    def test_second_size__setter(self):

        with self.assertRaises(ValueError):
            s4 = Square(5)
            s4.size = -3


if __name__ == '__main__':
    unittest.main()
