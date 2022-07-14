num = int(input())
res = []
aux = ''

for _ in range(1, num + 1):
    res.append(input())

k = int(input())

for i in range(num):
    if len(res[i]) >= k:
        aux += res[i][k-1:k]
    else:
        aux += ''

print(aux)
