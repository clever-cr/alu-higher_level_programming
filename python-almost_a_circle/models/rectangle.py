#!/usr/bin/python3
"""class rectangle"""
from models.base import Base


class Rectangle(Base):
    """class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """define class rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise valueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(Self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise valueError("height must be > 0")
        else:
            self.__height = value
    
    @property
    def x(self)
        return self.__x
    
    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise valueError("x must be >= 0")
        else:
            self.__x = value

@property
def y(self):
    return self.__y

@y.setter
def y(self, value):
    if type(value) != int:
        raise TypeError("y must be an integer")
    elif value < 0:
        raise valueError("y must be >= 0")
    else:
        self.__y = value
