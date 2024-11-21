a = int(input())
b = int(input())
c = int(input())
def count_matches(a, b, c):
    matches = 0
    if a == b:
        matches += 1
    if b == c:
        matches += 1
    if a == c:
        matches += 1
    return matches
if count_matches(a, b, c)==1:
    print(2)
else:
    print(count_matches(a, b, c))