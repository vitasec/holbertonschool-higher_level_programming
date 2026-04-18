#!/usr/bin/python3
"""
Contains append_write function
"""


def append_write(filename="", text=""):
    """
    Appends a string to a UTF8 text file and returns number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
