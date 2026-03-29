#!/usr/bin/python3
"""
Bu modul 'matrix_divided' funksiyasını təqdim edir.
"""


def matrix_divided(matrix, div):
    """
    Matrisin bütün elementlərini 'div' rəqəminə bölür.

    Arqumentlər:
        matrix: Tam ədəd və ya float-lardan ibarət siyahıların siyahısı.
        div: Bölən rəqəm (int və ya float).

    Qaytarır:
        Yeni matris (bölünmüş və 2 rəqəmə qədər yuvarlaqlaşdırılmış).
    """
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    msg_size = "Each row of the matrix must have the same size"

    # 1. Matris və daxili elementlərin tip yoxlanışı
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg_type)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg_type)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg_type)

    # 2. Sətirlərin ölçü yoxlanışı
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError(msg_size)

    # 3. div yoxlanışı
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 4. Yeni matrisin yaradılması (List Comprehension)
    return [[round(element / div, 2) for element in row] for row in matrix]
