def find_angle(H, M, S):
    total_seconds = H * 3600 + M * 60 + S
    total_degrees = total_seconds / 21600 * 360
    return total_degrees / 2
H = int(input())
M = int(input())
S = int(input())
angle = find_angle(H, M, S)
print(angle)
