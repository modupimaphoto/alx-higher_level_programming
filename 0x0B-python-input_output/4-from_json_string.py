#!/usr/bin/python3
"""Defines Python data structure module"""
import json


def from_json_string(my_str):
    """from_json_string function
    returns an object (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
