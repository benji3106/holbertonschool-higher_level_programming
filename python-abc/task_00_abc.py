#!/usr/bin/python3
"""
This module defines an abstract class Animal and its subclasses Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class that defines an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Returns the sound of the animal.
        """
        pass


class Dog(Animal):
    """
    Class that defines a Dog, subclass of Animal.
    """

    def sound(self):
        """
        Returns the sound of a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Class that defines a Cat, subclass of Animal.
    """

    def sound(self):
        """
        Returns the sound of a cat.
        """
        return "Meow"
