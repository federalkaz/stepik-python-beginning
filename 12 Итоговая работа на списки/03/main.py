string = input().split()

summa = 0
for number in string:
    summa += int(number)
print(*string, sep='+', end='=')
print(summa)
