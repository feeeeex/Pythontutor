def calculate_time_passed(alpha):
    hours = int(alpha // 30)
    remaining_angle = alpha - (hours * 30)
    minutes = int(remaining_angle // 0.5)
    remaining_angle_after_minutes = remaining_angle - (minutes * 0.5)
    seconds = int(remaining_angle_after_minutes / (1 / 120))
    return hours, minutes, seconds
alpha = float(input())
hours, minutes, seconds = calculate_time_passed(alpha)
print(hours, minutes, seconds)
