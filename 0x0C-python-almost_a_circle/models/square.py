#!/usr/bin/python3
from models.rectangle import Rectangle
"""Defines Square module"""


class Square(Rectangle):
    """Square class body"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        rep = "[Square] ({}) {}/{} - {}"
        return rep.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """return the width"""
        return self.width

    @size.setter
    def size(self, value):
        """set the width and height"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the class Square"""

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        rep_dict = {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
        return rep_dict
