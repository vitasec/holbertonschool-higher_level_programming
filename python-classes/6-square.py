#!/usr/bin/python3
"""Bu modul ölçüsü,  Square sinfini təyin edir."""


class Square:
    """Kvadratı təmsil edən sinif."""

    def __init__(self, size=0, position=(0, 0)):
        """Kvadratın yeni bir instansını yaradır.

        Args:
            size (int): Kvadratın tərəfinin uzunluğu. Standart 0-dır.
            position (tuple): Kvadratın (x, y) koordinatları.
                Standart (0, 0)-dır.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Ölçünü qaytarır."""
        return self.__size

    @size.setter
    def size(self, value):
        """Ölçünü təyin edir və yoxlayır."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Mövqeyi (koordinatları) qaytarır."""
        return self.__position

    @position.setter
    def position(self, value):
        """Mövqeyi təyin edir və yoxlayır.

        Args:
            value (tuple): Kvadratın yeni (x, y) mövqeyi.

        Raises:
            TypeError: Əgər value 2 müsbət ədəddən ibarət tuple deyilsə.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Sahəni hesablayır."""
        return self.__size ** 2

    def my_print(self):
        """Kvadratı '#' simvolu ilə çap edir."""
        if self.__size == 0:
            print()
            return

        # Y oxu üzrə sürüşdürmə (boş sətirlər)
        for _ in range(self.__position[1]):
            print()
        # X oxu üzrə sürüşdürmə və kvadratın çəkilməsi
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
