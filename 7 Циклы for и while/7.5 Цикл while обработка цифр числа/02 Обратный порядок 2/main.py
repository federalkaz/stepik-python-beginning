num = int(input())

while num > 0:
    aux = num % 10
    print(aux, sep='', end='')
    num = num // 10
