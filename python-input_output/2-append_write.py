#!/usr/bin/python3
"""
Module that defines a function that appends a string to a
UTF-8 text file and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Append a string to a UTF-8 text file and return the number
    of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
