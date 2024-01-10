#!/usr/bin/python3
"""class-to-JSON module."""


def class_to_json(obj):
    """class_to_json function
    agrs:
        obj is an instance of a Class
    """
    return obj.__dict__
