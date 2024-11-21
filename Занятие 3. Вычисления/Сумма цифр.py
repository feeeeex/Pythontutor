def find_sum(number):
    number_str = str(number)
    sum = 0
    for digit in number_str:
        sum += int(digit)
    return sum
number = int(input())
sum = find_sum(number)
print(sum)
