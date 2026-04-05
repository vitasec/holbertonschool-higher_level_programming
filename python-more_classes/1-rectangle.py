#!/usr/bin/python3
"""
Bu duzbucaqli
"""


class Rectangle:
    """Düzbucaqlı sinif."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Düzbucaqlının enini (width) qaytarır."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        enini yoxla return
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return et hundurluku"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        hundurluyun
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
