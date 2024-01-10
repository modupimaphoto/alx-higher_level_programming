#!/usr/bin/python3
from models.base import Base
"""Defines Rectangle module"""


class Rectangle(Base):
    """Rectangle class body"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        self.__width = value

    @property
    def height(self):
        """returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""
        self.__height = value

    @property
    def x(self):
        """returns the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        self.__x = value

    @property
    def y(self):
        """returns y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        self.__y = value
