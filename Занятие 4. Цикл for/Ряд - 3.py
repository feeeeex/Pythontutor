def print_odd_numbers(a, b):
    if a % 2 == 0:
        a -= 1
    for i in range(a, b-1, -2):
        print(i)
a = int(input())
b = int(input())
print_odd_numbers(a, b)