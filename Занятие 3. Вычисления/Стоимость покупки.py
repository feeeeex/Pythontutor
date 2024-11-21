def total_cost(a, b, n):
    total_cost_in_kopecks = n * (a * 100 + b)
    rubles = total_cost_in_kopecks // 100
    kopecks = total_cost_in_kopecks % 100
    return rubles, kopecks
a = int(input())
b = int(input())
n = int(input())
total_cost = total_cost(a, b, n)
print(total_cost[0], total_cost[1])
