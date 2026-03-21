#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Siayhini tersine capa ver"""
    if my_list:
        for i in reversed(my_list):
            print("{:d}".format(i))
