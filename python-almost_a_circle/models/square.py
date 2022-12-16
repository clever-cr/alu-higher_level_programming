#!/usr/bin/python3
""" define class square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """define class"""
        super().__init__(size,size,x,y,id)

    @property
    def size(self):
        """return size"""
        return self.width
    
    @size.setter
    def size(self, value):
        """set size"""
        self.width = value
        self.height = value