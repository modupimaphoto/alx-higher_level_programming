#!/usr/bin/python3
"""Defines read file module"""


def read_file(filename=""):
    """read_file function
    reads a text file (UTF8) and prints it result to stdout
    """
    with open(filename, "r") as file:
        content = file.read()
        print(content, end="")
