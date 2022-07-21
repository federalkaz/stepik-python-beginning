number = int(input())
res = [i ** 2 for i in range(1, number + 1)]

print(*res, sep='\n')
