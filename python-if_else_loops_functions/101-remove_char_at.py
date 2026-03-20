#!/usr/bin/python3
def remove_char_at(str, n):
    """Metnden  indexdekisimvolu silib qyatriri"""
    if n < 0 or n >= len(str):
        return str
    return str[:n] + str[n+1:]
