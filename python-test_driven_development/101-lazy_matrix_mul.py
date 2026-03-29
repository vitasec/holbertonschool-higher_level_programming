#!/usr/bin/python3
"""
Bu modul `lazy_matrix_mul` funksiyasını təqdim edir.
NumPy modulundan istifadə edərək iki matrisin hasilini tapır.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    NumPy istifadə edərək iki matrisi vurur.
    Əvvəlcə daxil olan məlumatları NumPy array-inə çeviririk ki, 
    kənar hallarda (edge cases) standart riyazi xətalar qaytarsın.

    Arqumentlər:
        m_a (list of lists): Birinci matris
        m_b (list of lists): İkinci matris

    Qaytarır:
        NumPy ndarray: Matrislərin hasili
    """
    return np.matmul(np.array(m_a), np.array(m_b))
