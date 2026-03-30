#!/usr/bin/python3
"""Bu modul ölçüsü Square sinfini təyin edir."""


class Square:
    """Kvadratı təmsil edən sinif."""

    def __init__(self, size=0):
        """Kvadratın yeni bir instansiyasını yaradır.

        Args:
            size (int, float): Kvadratın tərəfinin uzunluğu. Standart 0.
        """
        self.size = size

    @property
    def size(self):
        """Ölçünü qaytarır."""
        return self.__size

    @size.setter
    def size(self, value):
        """Ölçünü təyin edir və yoxlayır (həm int, həm də float üçün)."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Sahəni hesablayır və qaytarır."""
        return self.__size ** 2

    def __eq__(self, other):
        """== (bərabərdir) operatoru üçün müqayisə."""
        return self.area() == other.area()

    def __ne__(self, other):
        """!= (bərabər deyil) operatoru üçün müqayisə."""
        return self.area() != other.area()

    def __lt__(self, other):
        """< (kiçikdir) operatoru üçün müqayisə."""
        return self.area() < other.area()

    def __le__(self, other):
        """<= (kiçik və ya bərabərdir) operatoru üçün müqayisə."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """> (böyükdür) operatoru üçün müqayisə."""
        return self.area() > other.area()

    def __ge__(self, other):
        """>= (böyük və ya bərabərdir) operatoru üçün müqayisə."""
        return self.area() >= other.area()
