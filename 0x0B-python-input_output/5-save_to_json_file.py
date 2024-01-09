#!/usr/bin/python3
"""Defines writes file module"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file function
    writes an Object to a text file, using a JSON representation
    """
    with open(filename, "w") as file:
        content = json.dumps(my_obj)
        file.write(content)
