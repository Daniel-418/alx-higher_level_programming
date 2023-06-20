#!/usr/bin/python3
"""A rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the class"""
        super().__init__(id)
        Rectangle._validate_int("width", width)
        Rectangle._validate_int("height", height)
        Rectangle._validate_int("x", x)
        Rectangle._validate_int("y", y)
        Rectangle._validate_under_or_equals_zero("height", height)
        Rectangle._validate_under_or_equals_zero("width", width)
        Rectangle._validate_under_zero("y", y)
        Rectangle._validate_under_zero("x", x)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def x(self):
        """gets the value for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value for x"""
        Rectangle._validate_int("x", value)
        Rectangle._validate_under_zero("x", value)
        self.__x = value

    @property
    def y(self):
        """gets the value for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value for y"""
        Rectangle._validate_int("y", value)
        Rectangle._validate_under_zero("y", value)
        self.__y = value

    @property
    def width(self):
        """gets the value for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value for width"""
        Rectangle._validate_int("width", value)
        Rectangle._validate_under_or_equals_zero("width", value)
        self.__width = value

    @property
    def height(self):
        """gets the height's value"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height's value"""
        Rectangle._validate_int("height", value)
        Rectangle._validate_under_or_equals_zero("height", value)
        self.__height = value

    def area(self):
        """returns the area of this rectangle"""
        return self.__width * self.__height

    def display(self):
        """displays this rectangle"""

        """handling the y coordinates"""
        for a in range(self.__y):
            print("")

        for i in range(self.__height):
            """handling the x coordinates"""
            for j in range(self.__x):
                print(" ", end="")

            """printing the rectangle"""
            for k in range(self.__width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """assigns a value for each property"""
        if len(args) > 0 and args:
            control = 0
            for arg in args:
                if control == 0:
                    self.id = arg
                elif control == 1:
                    self.width = arg
                elif control == 2:
                    self.height = arg
                elif control == 3:
                    self.x = arg
                elif control == 4:
                    self.y = arg
                control += 1
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def __str__(self):
        """string method for this classs"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    """Utility Methods"""
    def _validate_int(name, value):
        """validates if input is an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    def _validate_under_zero(name, value):
        """validates if input is less than 0"""
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def _validate_under_or_equals_zero(name, value):
        """validates if input is under or equals to 0"""
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))
