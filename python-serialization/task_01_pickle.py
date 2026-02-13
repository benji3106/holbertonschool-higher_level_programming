#!/usr/bin/python3
"""
Module for serializing and deserializing a custom object using pickle
"""

import pickle


class CustomObject:
    """
    A simple custom class for demonstrating pickling.
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance and save it to a file.

        Returns True if successful, None otherwise.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
            return True
        except (FileNotFoundError, pickle.PickleError, OSError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a file and return an instance of CustomObject.

        Returns the object if successful, None otherwise.
        """
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
        except (FileNotFoundError, pickle.PickleError, EOFError, OSError):
            return None
