#!/usr/bin/python3
"""prints the list, but sorted (ascending sort)"""


class MyList(list):
    """Class methods and attributes"""

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
