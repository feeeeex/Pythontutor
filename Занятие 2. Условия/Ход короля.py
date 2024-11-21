def can_move(a1, b1, a2, b2):
    if abs(a1 - a2) <= 1 and abs(b1 - b2) <= 1:
        return "YES"
    else:
        return "NO"
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
print(can_move(a1, b1, a2, b2))
