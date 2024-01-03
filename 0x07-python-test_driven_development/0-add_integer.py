#!/usr/bin/python3

"""
    The '0-add_integer' returns the sum oof two numbers
    a: The first parameter.
    b: The second parameter.
"""
def add_integer(a, b=98):
    """
        Works with numbers - int
    """
    if isinstance(a, int) or isinstance(a, float):
        int(a)
    else:
        raise TypeError("a must be an integer")

    if isinstance(b, int) or isinstance(b, float):
        int(b)
    else:
        raise TypeError("b must be an integer")

    sum = a + b

    return int(sum)
