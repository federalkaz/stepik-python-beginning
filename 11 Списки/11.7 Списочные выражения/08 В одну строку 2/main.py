symbols = list(input())

print(*[i for i in symbols if i in '0123456789'], sep='')
