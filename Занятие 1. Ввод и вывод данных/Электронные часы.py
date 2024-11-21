n=int(input())
if n//60 == 24:
    print(0, n % 60)
elif n < 24 * 60:
    print(n//60, n % 60)
else:
    while n > 24*60:
        n = n - 24 * 60
    print(n//60, n % 60)