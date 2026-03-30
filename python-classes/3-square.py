#!/usr/bin/python3
"""Bu modul square ucun"""


class Square:
    """Kvadratı təmsil edən sinif."""

    def __init__(self, size=0):
        """Kvadratın yeni instance yarat

        Args:
            size (int): Kvadratın terefin uzunlugu default zerodu

        Raises:
            TypeError: Əgər size tam ədəd (integer) deyilsə.
            ValueError: Əgər size 0-dan kiçikdirsə.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Kvadratın saheni tapir

        Returns:
            int: Kvadratın sahesi
        """
        return self.__size ** 2
