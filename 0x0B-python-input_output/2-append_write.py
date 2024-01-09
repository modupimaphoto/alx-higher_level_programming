#!/usr/bin/python3
"""Defines append file module"""


def append_write(filename="", text=""):
    """append_write function
     appends a string at the end of a text file
     returns the number of characters added
     """

    with open(filename, "a") as file:
        file.write(text)
    return len(text)
