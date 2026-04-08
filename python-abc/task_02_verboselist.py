#!/usr/bin/python3
"""module that defines a Verboselist Class"""


class VerboseList(list):
    """define a class that named VerboseList"""
    def append(self, item):
        """Adds an item to the list and prints a confirmation message."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """method that extend an item to the list"""
        num_item = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{num_item}] items.")

    def remove(self, item):
        """method that remove an item to the list"""
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index = -1):
        """method that pop an item to the list"""
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
