#!/usr/bin/python3
def uniq_add(my_list=[]):
    # 1. Siyahını set-ə çeviririk (təkrarlar silinir)
    # 2. sum() funksiyası ilə cəmləyirik
    return sum(set(my_list))
