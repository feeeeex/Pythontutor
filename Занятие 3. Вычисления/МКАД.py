def position(v, t):
    position = v * t
    return position % 109
v = int(input())
t = int(input())
print(position(v, t))
