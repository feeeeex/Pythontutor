N = int(input())
cards = [int(input()) for _ in range(N-1)]
for i in range(1, N+1):
    if i not in cards:
        print(i)
        break