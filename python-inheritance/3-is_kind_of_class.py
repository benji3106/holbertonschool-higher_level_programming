#!/usr/bin/python3
"""Module that defines is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance of a class or its subclasses."""
    return isinstance(obj, a_class)
