#!/usr/bin/python3
"""Square class definition"""

class Square:
    """Square class body"""

    def __init__(self, size=0):
        """
        Intialize a new Square.
        Args: size (int): The size of the new square
        """
        self.__size = size

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
