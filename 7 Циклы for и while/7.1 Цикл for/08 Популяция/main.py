m, p, n = int(input()), int(input()), int(input())

for i in range(n):
    print(i + 1, float((1 + p / 100) ** i * m))
