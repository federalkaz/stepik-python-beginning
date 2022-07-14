strings = input().split()
res = []

for out in strings:
    res += out[0]

print(res[0], res[1], res[2], sep='.', end='.')
