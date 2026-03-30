#!/usr/bin/python3
"""Bu modul kavdrat sinif"""


class Square:
    """Kvadratı sinifi"""

    def __init__(self, size=0):
        """Kvadratın instancesi yaratiriq

        Args:
            size (int): Kvadratın terefini uzunlguu

        Raises:
            TypeError: Əgər size tam ede deyilse
            ValueError: Əgər size menfidirse
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
