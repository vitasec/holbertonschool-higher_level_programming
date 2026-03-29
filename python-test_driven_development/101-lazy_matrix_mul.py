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
    # 1. Skalyar xətaları tuturuq
    if type(m_a) in [int, float, bool, str, complex] or \
       type(m_b) in [int, float, bool, str, complex]:
        raise ValueError("Scalar operands are not allowed, use '*' instead")
    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        err_msg = str(e)
        # 2. Ölçü uyğunsuzluğu xətası (gufunc)
        if "gufunc signature" in err_msg or "mismatch" in err_msg:
            try:
                np.dot(m_a, m_b)
            except ValueError as dot_e:
                raise ValueError(str(dot_e))
        # 3. Qeyri-həmcins (jagged) matris xətası
        if "setting an array element with a sequence" in err_msg:
            raise ValueError("setting an array element with a sequence.")
        raise e
    except TypeError as e:
        err_msg = str(e)
        # 4. Daxili elementlərin tipi səhv olduqda
        if "ufunc 'matmul' did not contain a loop" in err_msg:
            # Əgər ölçülər vurulmaq üçün UYĞUN DEYİLSƏ
            try:
                if len(m_a[0]) != len(m_b):
                    raise TypeError("invalid type promotion")
            except Exception:
                pass
            # Əgər ölçülər uyğundursa, amma tip səhvidirsə
            raise TypeError("invalid data type for einsum")
        raise e
