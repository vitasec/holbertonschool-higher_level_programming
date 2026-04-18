#!/usr/bin/python3
"""
Bu yazmaq metni
"""


def write_file(filename="", text=""):
    """
    Bir .
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
