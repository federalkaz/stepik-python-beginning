num = int(input())
max, min = 0, 9

while num > 0:
    aux = num % 10
    num = num // 10
    if aux > max:
        max = aux
    if aux < min:
        min = aux

print('Максимальная цифра равна', max)
print('Минимальная цифра равна', min)
