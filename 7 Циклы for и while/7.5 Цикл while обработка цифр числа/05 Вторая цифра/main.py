num = int(input())
i = 1

while num >= 10:
    i += 1
    aux = num % 10
    num = num // 10
    digit = num // (10 ** (i - 1))

print(aux)
