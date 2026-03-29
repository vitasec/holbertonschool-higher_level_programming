#!/usr/bin/python3
"""
Bu modul 'add_integer' funksiyasını təqdim edir.
Funksiya iki rəqəmi toplayır və nəticəni tam ədəd kimi qaytarır.
"""


def add_integer(a, b=98):
    """
    İki tam ədədi (və ya float-u cast edərək) toplayır.

    Arqumentlər:
    a: birinci rəqəm (int və ya float)
    b: ikinci rəqəm (int və ya float, default olaraq 98)

    Qaytarır:
    a + b cəminin tam ədəd (int) qarşılığı.

    Xətalar:
    TypeError: Əgər a və ya b integer/float deyilsə.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Float gələrsə int-ə çeviririk (casting)
    return int(a) + int(b)
