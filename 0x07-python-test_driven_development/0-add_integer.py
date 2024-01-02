#!/usr/bin/python3

def add_integer(a, b=98):

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
