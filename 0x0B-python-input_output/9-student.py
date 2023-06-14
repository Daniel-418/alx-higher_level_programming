#!/usr/bin/python3
"""Contains a student class"""
import json


class Student:
    """A student class"""

    def __init__(self, first_name, last_name, age):
        """initializes this student"""
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self):
        """Retrieves the dict repr of this student"""
        return self.__dict__
