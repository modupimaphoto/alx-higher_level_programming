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
