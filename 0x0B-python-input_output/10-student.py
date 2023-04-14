#!/usr/bin/python3
"""Contains the student class"""


class Student:
    """A class describing a student"""

    def __init__(self, first_name, last_name, age):
        """initializes this student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves the dict representation of this student"""
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    my_dict[i] = self.__dict__[i]

            return my_dict

