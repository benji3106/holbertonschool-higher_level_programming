#!/usr/bin/python3
"""This module defines a FlyingFish class that inherits from Fish and implements the fly method."""


class Fish:
    """Base class for fish."""

    def swim(self):
        """Simulate swimming."""
        print("The fish is swimming.")
    def habitat(self):
        """Return the habitat of the fish."""
        print("The fish lives in water.")
    
class Bird:
    """Base class for birds."""

    def fly(self):
        """Simulate flying."""
        print("The bird is flying")
    def habitat(self):
        """Return the habitat of the bird."""
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """Class representing a flying fish, inheriting from Fish and Bird."""

    def fly(self):
        """Override the fly method to simulate flying."""
        print("The flying fish is soaring!")
    
    def swim(self):
        """Override the swim method to simulate swimming."""
        print("The flying fish is swimming!")
    
    def habitat(self):
        """Override the habitat method to return the habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")
