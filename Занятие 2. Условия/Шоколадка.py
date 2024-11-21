def can_break_chocolate(n, m, k):
    total_pieces = n * m
    if k < total_pieces and (k % m == 0 and k // m < n or k % n == 0 and k // n < m):
        return "YES"
    return "NO"
n = int(input())
m = int(input())
k = int(input())
print(can_break_chocolate(n, m, k))
