#!/usr/bin/python3
"""Defines creates an Object module"""
import json


def load_from_json_file(filename):
    """load_from_json_file function
     creates an Object from a “JSON file”
     """
    with open(filename, "r") as file:
        content = json.loads(file.read())
    return content
