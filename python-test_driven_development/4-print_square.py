#!/usr/bin/python3
"""function print square"""


def print_square(size):
    """prints square with character #"""
    if type(size) != int:
        error1 = 'size must be an integer'
        raise ValueError(error1)
    elif size < 0:
        error2 = 'size must be >= 0'
        raise ValueError(error2)
    if size == 0:
        return
    else:
        for i in range(size):
            print("#" * size)
