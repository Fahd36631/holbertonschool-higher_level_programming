#!/usr/bin/python3
"""Defines a function that checks if an object is an instance of a class
or an instance of a class that inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or a subclass of it,
    otherwise False.
    """
    return isinstance(obj, a_class)
