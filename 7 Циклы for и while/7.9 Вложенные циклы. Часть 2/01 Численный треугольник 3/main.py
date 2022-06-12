number = int(input())
i, j = 0, 0

for i in range(number):
    i += 1
    for _ in range(i):
        j += 1
        print(j, end=' ')
    print()
