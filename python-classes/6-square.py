#!/usr/bin/python3
"""class square"""


class Square:
    """ class Square"""
    def __init__(self, size=0):
        """init size"""
        self.__size = size
    
    def __init__(self, position=(0,0)):
        """init position"""
        self.__position = position

    @property
    def size(self):
        "size attribute"
        return self.__size
    
   

    @size.setter
    def size(self, size):
        """ assigning"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise valueError("size must be >= 0")


    @property
    def position(self)
        """ retrieve position"""
        return self.__position

    @position.setter
    def position(self, val):
        """ assign position to a value"""
    self.__position = val
        if not isinstance(val, tuple) or len(val) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(val[0], int) or not isinstance(val[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if val[0] < 0 or val[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        sarea = self.__size * self.__size
        return sarea

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for v in range(self.__position[1]):
                print()
            for s in range(self.__size):
                for k in range(self.__position[0]):
                    print('', end="")
                for i in range(self.__size):
                    print("#", end="")
                print()

