#!/usr/bin/python3
"""define class rectangle"""


class Rectangle:

    """class Rectangle"""
    def __init__(self, width=0):
        """initialize width"""
        self.width = width

    def __init__(self, height=0):
        """initialize height"""
        self.height = height

    @property
    def width(self):
        """"retrieve width"""
        return self.__width

    @width.setter
    def width(Self, value):
        """ sets width"""
        self.___width = value
        if not isinstance(value, int):
            raise TypeErro("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """define height"""
        return self.___height

    @height.setter
    def height(self, value):
        """assign height"""
        self.___height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
