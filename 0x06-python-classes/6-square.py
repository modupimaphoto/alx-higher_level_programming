#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Square class body"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Intialize a new Square.
        Args: size (int): The size of the new square
        """
        self.__position = position

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """Retrieve the currect Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the new Square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                if not self.__position[1] > 0:
                    print("_" * self.__position[0], "#" * self.__size)

    def position(self):
        """Returns the current position"""
        return self.__position

    def position(self, value):
        """Set new position"""
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
