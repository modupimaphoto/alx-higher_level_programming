#!/usr/bin/python3
"""Square class definition"""

class Square:
    """Square class body"""

    def __init__(self, size=0):
        """
        Intialize a new Square.
        Args: size (int): The size of the new square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area"""
        return self.__size ** 2
