#!/usr/bin/python3
"""Function that adds 2 numbers"""


def add_integer(a, b=98):
    """add a and b"""
    if type(a) != float and type(a) != int:
        error = "a must be an integer"
        raise TypeError(error)
    elif type(b) != float and type(b) != int:
        error2 = "b must be an integer"
        raise TypeError(error2)
    return int(a) + int(b)
