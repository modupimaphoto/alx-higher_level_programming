#!/usr/bin/python3
"""Magic class definition"""
import math


class MagicClass:
    """Initialize of MagicClass"""

    def __init__(self, radius=0):
        self._MagicClass__radius = 0

        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")

        self._MagicClass__radius = radius

        def area(self):
            """Calculates the area"""
            return self._MagicClass__radius ** 2 * math.pi

        def cirm(self):
            """Calculates the circumference"""
            return 2 * math.pi * self._MagicClass__radius
