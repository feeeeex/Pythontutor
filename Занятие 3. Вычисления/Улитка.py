def days_to_reach_top(h, a, b):
    days = 0
    current_height = 0
    while current_height < h:
        current_height += a
        if current_height >= h:
            break
        current_height -= b
        days += 1
    return days
h = int(input())
a = int(input())
b = int(input())
print(days_to_reach_top(h, a, b)+1)
