#!/usr/bin/python3
"""A module to define a rectangle class"""


class Rectangle:
    """defines the rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes the class"""
        if height < 0 or width < 0:
            raise ValueError("Height and width must be >= 0")
        if type(height) is not int or type(width) is not int:
            raise TypeError("Height and width must be an integer")

        self.__width = width
        self.__height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        self.__width = width

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets the value for the height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height

    def area(self):
        """returns the are of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of this rectangle"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of this Rectangle"""
        string = ""

        if self.__width == 0 or self.__height == 0:
            return string
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    string = string + str(self.print_symbol)
                string = string + "\n"

        return string

    def __repr__(self):
        """Returns a string representation that can be used
        to create another object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """"Show a message when a rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False or \
           isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
