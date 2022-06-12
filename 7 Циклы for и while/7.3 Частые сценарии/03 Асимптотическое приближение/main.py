from math import *
num = int(input())

total = 1
for i in range(2, num + 1):
    total += 1 / i

print(total - log(num))
