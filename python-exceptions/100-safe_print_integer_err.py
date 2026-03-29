#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        # Dəyişəni integer kimi çap etməyə çalışırıq
        print("{:d}".format(value))
        return True
    except Exception as e:
        # Xətanı stderr-ə çap edirik
        # 'file=sys.stderr' arqumenti çapın hara gedəcəyini təyin edir
        print("Exception: {}".format(e), file=sys.stderr)
        return False
