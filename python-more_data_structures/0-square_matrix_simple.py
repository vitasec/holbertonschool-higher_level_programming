#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Yeni bir matris yaradırıq: hər sətirdəki hər bir x-in kvadratını al
    return [[x**2 for x in row] for row in matrix]