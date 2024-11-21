def calculate_angle(alpha):
    hours = alpha / 30
    minutes = (hours - int(hours)) * 60
    angle = minutes * 6
    return angle
alpha = float(input())
print(calculate_angle(alpha))