def lesson_end_time(lesson_number):
    start_hour = 9
    start_minute = 45
    lesson_duration = 45
    break_1_duration = 5
    break_2_duration = 15
    lesson_start_hour = start_hour
    lesson_start_minute = start_minute
    for i in range(1, lesson_number):
        lesson_start_minute += lesson_duration
        if i % 2 == 0:
            lesson_start_minute += break_2_duration
        else:
            lesson_start_minute += break_1_duration
    if lesson_start_minute >= 60:
        lesson_start_hour += lesson_start_minute // 60
        lesson_start_minute %= 60
    return lesson_start_hour, lesson_start_minute
lesson_number = int(input())
end_hour, end_minute = lesson_end_time(lesson_number)
print(end_hour, end_minute, )
