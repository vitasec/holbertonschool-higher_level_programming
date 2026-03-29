#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Siyahının i-ci elementini integer kimi çapi
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Əgər element integer ddeyilse davam
            continue
    print("")  # Sonda yeni sətir
    return count
