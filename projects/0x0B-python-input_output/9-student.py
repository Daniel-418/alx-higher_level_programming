#!/usr/bin/python3
"""Contains the student class"""


class Student:
    """A class describing a student"""

    def __init__(self, first_name, last_name, age):
        """initializes this student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves the dict representation of this student"""
        return self.__dict__
