symbols = input().split()

print(*[int(i) ** 2 for i in symbols if int(i) ** 2 % 2 == 0 and int(i) ** 2 % 10 != 4])
