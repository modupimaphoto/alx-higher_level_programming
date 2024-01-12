#!/usr/bin/python3
import json
"""Defines base module"""


class Base:
    """Base class body"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor attributes"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries:
        Args:
            list_dictionaries is a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '"[]"'
        return json.dumps(list_dictionaries)
