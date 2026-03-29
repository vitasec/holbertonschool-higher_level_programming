#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    numerator = 0  # Sürət (score * weight cəmi)
    denominator = 0  # Məxrəc (weight cəmi)
    for tup in my_list:
        numerator += tup[0] * tup[1]
        denominator += tup[1]
    return numerator / denominator
