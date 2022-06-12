num = int(input())
total = 0
aux = 0
i = 1

while num > 0:
    if num >= 25:
        aux = num // 25
        total += aux
        num -= aux * 25
        aux = 0
    if num >= 10:
        aux = num // 10
        total += aux
        num -= aux * 10
        aux = 0
    if num >= 5:
        aux = num // 5
        total += aux
        num -= aux * 5
        aux = 0
    if num >= 1:
        aux = num // 1
        total += aux
        num -= aux * 1
        aux = 0

print(total)
