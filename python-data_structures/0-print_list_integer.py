#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Siyahdaki  ədədləri çap edən ."""
    for i in range(len(my_list)):
        # str.format() cevirem
        print("{:d}".format(my_list[i]))
