#!/usr/bin/python3
"""Module that defines a class LockedClass"""


class LockedClass:
    """A class that prevents dynamic attribute creation."""
    __slots__ = ['first_name']
