def days_to_travel(n, m):
    days = m // n
    if m % n != 0:
        days += 1
    return days
n = int(input())
m = int(input())
print(days_to_travel(n, m))
