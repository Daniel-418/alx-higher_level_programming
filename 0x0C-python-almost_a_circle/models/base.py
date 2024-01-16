#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """The Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the json string representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves the json repr to a file"""
        filename = cls.__name__ + ".json"
        dict_list = []

        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                for j in list_objs:
                    dict_list.append(j.to_dictionary())

                f.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """return the list of the json string representation"""
        json_list = []
        if json_string is None or len(json_string) == 0:
            return json_list
        else:
            json_list = json.loads(json_string)
            return json_list

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance from a dictionary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """loads from a file"""
        filename = cls.__name__ + ".json"
        new_list = []

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                dictionary_list = Base.from_json_string(f.read())
                for a in dictionary_list:
                    new_list.append(cls.create(**a))
                return new_list
        except IOError:
            return []
