#!/usr/bin/env python3
"""Pickling custom classes with safe serialization/deserialization."""

import pickle


class CustomObject:
    """Custom object that supports pickling to/from a file."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in the required format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance to a pickle file.

        Return None if the file can't be written or serialization fails.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError, AttributeError, TypeError):
            return None
        return filename

    @classmethod
    def deserialize(cls, filename):
        """Deserialize and return a CustomObject instance from a pickle file.

        Return None if the file doesn't exist, is malformed, or can't be read.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
        except (OSError, EOFError, pickle.UnpicklingError, pickle.PickleError):
            return None
        return None
