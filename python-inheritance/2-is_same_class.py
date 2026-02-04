#!/usr/bin/python3
"""Module that defines is_same_class function."""


def is_same_class(obj, a_class):
    """Check if object is exactly an instance of a given class."""
    return type(obj) is a_class
