#!/usr/bin/python3
"""Rectangle  Module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square body"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
