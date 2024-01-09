#!/usr/bin/python3
"""Defines writes file module"""


def write_file(filename="", text=""):
    """write_file function
    writes a string to a text file
    returns the number of characters written
    """

    with open(filename, "w") as file:
        file.write(text)
    return len(text)
