#!/usr/bin/python3
""" define class square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """define class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """return size"""
        return self.width
    
    @size.setter
    def size(self, value):
        """set size"""
        self.width = value
        self.height = value

    def __str__(self):
        """string representation"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,self.y,self.size))

    def update(self, *args, **kwargs):
        """update class square"""
        try:
            if len(args) != 0:
                try:
                    self.id = args[0]
                    self.size = args[1]
                    self.x = args[2]
                    self.y = args[3]
                except IndexError:
                    pass

            else:
                try:
                    self.x = kwargs.get('size')
                except Exception:
                    pass
                try:
                    self.x = kwargs.get('x')
                except Exception:
                    pass
                try:
                    self.y = kwargs.get('y')
                except Exception:
                    pass
                try:
                    self.id = kwargs['id']
                except Exception:
                    pass
        except Exception:
            pass
    
    def to_dictionary(self):
        """dictionary representation"""
        return {"id": self.id, "size": self.size, "x":self.x, "y":self.y}
