number = int(input())
i, j = 0, 0

for i in range(number):
    i += 1
    for j in range(i):
        j += 1
        print(j, end='')
    for _ in range(j - 1):
        j -= 1
        print(j, end='')
    print()
