#!/usr/bin/python3
"""Defines a function that returns the available attributes and methods of an
object.
"""


def lookup(obj):
    """Returns a list containing the attributes and methods of an object."""
    return dir(obj)
