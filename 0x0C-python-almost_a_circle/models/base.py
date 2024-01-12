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
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """" writes the JSON string representation of
        list_objs to a file:
        Args:
            list_objs is a list of instances who inherits of Base
        """
        with open(f"{cls.__name__}.json", "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """eturns the list of the JSON string representation json_string:
        Args:
            json_string is a string representing a list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
