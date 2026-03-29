#!/usr/bin/python3
"""
Bu modul `matrix_mul` funksiyasını təqdim edir.
İki matrisi (siyahıların siyahısı) bir-birinə vurur və daxil olan
məlumatı xüsusi ardıcıllıqla yoxlayır.
"""


def matrix_mul(m_a, m_b):
    """
    İki matrisin hasilini tapır.

    Arqumentlər:
        m_a (list of lists): Birinci matris (int və ya float)
        m_b (list of lists): İkinci matris (int və ya float)

    Qaytarır:
        list of lists: Matrislərin hasili
    """
    # 1. 'list' yoxlanışı
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # 2. 'list of lists' yoxlanışı
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # 3. 'empty' yoxlanışı (boş siyahı)
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # 4. 'int və ya float' yoxlanışı
    for row in m_a:
        for el in row:
            if type(el) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for el in row:
            if type(el) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    # 5. 'rectangle' yoxlanışı (hər sətir eyni uzunluqdadırmı?)
    len_a = len(m_a[0])
    for row in m_a:
        if len(row) != len_a:
            raise TypeError("each row of m_a must be of the same size")
    len_b = len(m_b[0])
    for row in m_b:
        if len(row) != len_b:
            raise TypeError("each row of m_b must be of the same size")

    # 6. Matrislərin vurula bilməsi (m_a sütun sayı == m_b sətir sayı)
    if len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # --- Matris Vurma Əməliyyatı ---
    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(len(m_b[0])):
            sum_val = 0
            for k in range(len(m_b)):
                sum_val += m_a[i][k] * m_b[k][j]
            row_result.append(sum_val)
        result.append(row_result)

    return result
