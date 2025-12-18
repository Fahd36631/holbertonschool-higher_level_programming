#!/usr/bin/python3
"""Defines a function that checks if an object is an instance of a class
that inherited from a specified class.
"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a subclass of a_class,
    otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
