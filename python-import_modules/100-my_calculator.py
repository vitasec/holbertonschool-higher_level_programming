#!/usr/bin/python3
import sys
from my_calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    # Arqument sayini yoxla (fayl adi + 3 arqument = 4)
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Arqumentleri deyisenlere menimset
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Operatora gore funksiyani sec
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        # Yanlis operator xetasi
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Neticeni cap et
    print("{} {} {} = {}".format(a, operator, b, result))
