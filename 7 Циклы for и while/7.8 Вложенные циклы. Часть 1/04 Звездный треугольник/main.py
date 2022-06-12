number = int(input())
aux = number // 2 + 1

for i in range(1, aux + 1):
    for j in range(1, i + 1):
        print('*', end='')
    print()
for i in range(1, number - aux + 1):
    aux -= 1
    for j in range(1, aux + 1):
        print('*', end='')
    print()
