P = int(input())
X = int(input())
Y = int(input())
deposit = X * 100 + Y
interest = P / 100 * deposit
total_deposit = deposit + interest
rubles = int(total_deposit // 100)
kop = int(total_deposit % 100)
print(rubles, kop)
