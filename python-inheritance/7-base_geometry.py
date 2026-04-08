#!/usr/bin/python3
"""
A module that creates a class names BaseGeometry
"""


class BaseGeometry:
    """
    A class that raises an exception and checks if a value
    is an integer >0
    """
    def area(self):
        """
        Raise an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Check if value is an integer
        """
        if type(name) is not str:
            raise TypeError("{} must be a string".format(name))
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
