#!/usr/bin/python3
"""A square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes a square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "{} ({}) {}/{} - {}".format("Square",
                                           self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """gets the value of this square's size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the value for the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns a value for each property"""
        if len(args) > 0 and args:
            control = 0
            for arg in args:
                if control == 0:
                    self.id = arg
                elif control == 1:
                    self.width = arg
                    self.height = arg
                elif control == 2:
                    self.x = arg
                elif control == 3:
                    self.y = arg
                control += 1
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns a dictionary containing this square's attribute"""
        square_dict = {}
        square_dict['id'] = self.id
        square_dict['size'] = self.width
        square_dict['x'] = self.x
        square_dict['y'] = self.y

        return square_dict
