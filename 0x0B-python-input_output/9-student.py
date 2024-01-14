#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    """A Student class"""
    def __init__(self, first_name, last_name, age):
        """
        Constructor to initialize the class
        Args:
            first_name(str): The first name of the student
            last_name(str): The last name of the student
            age(int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a json representation of this object
        """
        return self.__dict__
