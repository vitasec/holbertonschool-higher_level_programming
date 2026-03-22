#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Iki tubulun ilk iki elemntini toplyan funcsiya"""
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    return (a[0] + b[0], a[1] + b[1])
