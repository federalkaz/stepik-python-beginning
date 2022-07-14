number = int(input())
aux1, aux2, res = [], [], []

for _ in range(number):
    aux1.append(input())

k = int(input())

for _ in range(k):
    aux2.append(input())

for string in aux1:
    for kk in aux2:
        if string.lower().find(kk.lower()) != -1:
            res.append(string)
# вывести уникальные строки

for string in res:
    print(string)
