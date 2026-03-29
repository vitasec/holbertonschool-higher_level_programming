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
    # 1. Skalyar (tək dəyər və ya sətir) xətalarını əvvəlcədən tuturuq
    if type(m_a) in [int, float, bool, str, complex] or \
       type(m_b) in [int, float, bool, str, complex]:
        raise ValueError("Scalar operands are not allowed, use '*' instead")
    # 2. Matrisləri vurmağa cəhd edirik
    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        err_msg = str(e)
        # 3. Ölçü xətası (gufunc) olduqda köhnə formata (np.dot) qaytarırıq
        if "gufunc signature" in err_msg or "mismatch" in err_msg:
            try:
                np.dot(m_a, m_b)
            except ValueError as dot_e:
                raise ValueError(str(dot_e))
        raise e
    except TypeError as e:
        err_msg = str(e)
        # 4. Daxili elementlərin
        if "ufunc 'matmul' did not contain a loop" in err_msg:
            raise TypeError("invalid data type for einsum")
        raise e
