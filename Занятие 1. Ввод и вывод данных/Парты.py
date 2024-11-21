a = int(input())
b= int(input())
c= int(input())
n=0
if a %2 == 1:
    n = n+1
if b %2 == 1:
    n = n+1
if c %2 == 1:
    n = n+1
n= n + a//2 + c//2 + b//2
print(n)