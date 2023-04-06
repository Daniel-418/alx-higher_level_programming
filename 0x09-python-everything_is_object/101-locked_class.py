#!/usr/bin/python3

"""Defines a locked class."""


class LockedClass:
    """A class that prevents objects from creating
    instance attributes"""

    __slots__ = ["first_name"]
