def first_decimal_digit(x):
    return int(str(x).split('.')[1][0])
x = float(input())
print(first_decimal_digit(x))