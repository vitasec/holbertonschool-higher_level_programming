#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        # Funksiyanı gələn arqumentlərlə çağırırıq
        result = fct(*args)
        return result
    except Exception as e:
        # Xəta baş verərsə stderr-ə yazırıq
        print("Exception: {}".format(e), file=sys.stderr)
        return None
