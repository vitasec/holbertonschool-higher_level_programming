#!/usr/bin/python3
"""Bu modul Square"""


class Square:
    """Kvadratı təmsil edən sinif."""

    def __init__(self, size=0):
        """Kvadratın yeni bir instansını (obyektini) yaradır.

        Args:
            size (int): Kvadratın tərəfinin uzunluğu. Standart olaraq 0-dır.
        """
        self.size = size

    @property
    def size(self):
        """Kvadratın mövcud ölçüsünü (size) əldə etmək üçün getter."""
        return self.__size

    @size.setter
    def size(self, value):
        """Kvadratın ölçüsünü təyin etmək üçün setter və yoxlayıcı.

        Args:
            value (int): Kvadratın yeni ölçüsü.

        Raises:
            TypeError: Əgər dəyər tam ədəd (integer) deyilsə.
            ValueError: Əgər dəyər 0-dan kiçikdirsə.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Kvadratın mövcud sahəsini hesablayır və qaytarır.

        Returns:
            int: Kvadratın sahəsi.
        """
        return self.__size ** 2

    def my_print(self):
        """Kvadratı '#' simvolu ilə standart çıxışa (stdout) çəkir.
        Əgər ölçü 0-a bərabərdirsə, sadəcə boş bir sətir çap edir.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
