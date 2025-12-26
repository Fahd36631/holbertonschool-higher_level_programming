#!/usr/bin/python3
"""Module for converting class instances to JSON."""


def class_to_json(obj):
    """Return a dictionary representation of an object."""
    return obj.__dict__
