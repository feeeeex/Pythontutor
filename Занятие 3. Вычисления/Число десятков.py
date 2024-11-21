def find_tens(number):
    number_str = str(number)
    if len(number_str) < 2:
        return 0
    tens = int(number_str[-2])
    return tens
number = int(input())
tens = find_tens(number)
print(tens)