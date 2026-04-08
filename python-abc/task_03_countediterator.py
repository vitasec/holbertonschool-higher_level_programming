#!/usr/bin/python3
"""module that defines a CountedIterator Class"""


class CountedIterator():
    def __init__(self, iterable):
        self.iter = iter(iterable)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.iter)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
