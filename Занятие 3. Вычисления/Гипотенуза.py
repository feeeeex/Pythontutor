import math
def find_hypotenuse(a, b):
    hypotenuse = math.sqrt(a**2 + b**2)
    return hypotenuse
a = int(input())
b = int(input())
hypotenuse = find_hypotenuse(a, b)
print(hypotenuse)
