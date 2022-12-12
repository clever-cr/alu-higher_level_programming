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
