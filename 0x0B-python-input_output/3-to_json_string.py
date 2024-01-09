#!/usr/bin/python3
"""Defines JSONrepresentation module"""
import json


def to_json_string(my_obj):
    """to_json_string function
    returns the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
