#!/usr/bin/python3
"""
Module that defines a function that returns the dictionary
description of an object for JSON serialization.
"""


def class_to_json(obj):
    """Return the dictionary description of an object."""
    return obj.__dict__
