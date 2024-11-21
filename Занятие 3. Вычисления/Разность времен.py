def time_difference(hour1, minute1, second1, hour2, minute2, second2):
    time1 = hour1 * 3600 + minute1 * 60 + second1
    time2 = hour2 * 3600 + minute2 * 60 + second2
    difference = abs(time2 - time1)
    return difference
hour1 = int(input())
minute1 = int(input())
second1 = int(input())
hour2 = int(input())
minute2 = int(input())
second2 = int(input())
print(time_difference(hour1, minute1, second1, hour2, minute2, second2))
