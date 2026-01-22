#!/usr/bin/python3
"""Module that provides a function to add two integers."""


def add_integer(a, b=98):
    """Return the addition of a and b as integers."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Reject NaN / Infinity (float overflow & invalid float values)
    if isinstance(a, float) and (a != a or a in (float("inf"), float("-inf"))):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b != b or b in (float("inf"), float("-inf"))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
