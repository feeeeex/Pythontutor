def check_colors(a1, b1, a2, b2):
    if (a1 + b1) % 2 == (a2 + b2) % 2:
        return "YES"
    else:
        return "NO"
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
print(check_colors(a1, b1, a2, b2))
