#!/usr/bin/python3
""" define class square"""

class Square(Rectangle):
    """class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """define class"""
        super().__init__(size,size,x,y,id)
