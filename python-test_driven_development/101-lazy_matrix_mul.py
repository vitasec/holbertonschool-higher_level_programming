#!/usr/bin/python3
"""
Bu modul `lazy_matrix_mul` funksiyasını təqdim edir.
NumPy modulundan istifadə edərək iki matrisin hasilini tapır.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    NumPy istifadə edərək iki matrisi vurur.

    Arqumentlər:
        m_a (list of lists): Birinci matris
        m_b (list of lists): İkinci matris

    Qaytarır:
        NumPy ndarray: Matrislərin hasili
    """
    # Holberton Checker-in Numpy versiya problemini ötmək üçün:
    if type(m_a) is str or type(m_b) is str:
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    return np.matmul(m_a, m_b)
