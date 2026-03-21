#!/usr/bin/python3
import sys
from my_calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    # Arqument sayını yoxla (fayl adı + 3 arqument = 4)
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Arqumentləri dəyişənlərə mənimsət
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Operatora görə funksiyanı seç
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Nəticəni çap et
    print("{} {} {} = {}".format(a, operator, b, result))
