#!/usr/bin/python3
"""Module that finds object attributes."""


def lookup(obj):
    """Returns a list of available attributes and methods."""
    return dir(obj)
