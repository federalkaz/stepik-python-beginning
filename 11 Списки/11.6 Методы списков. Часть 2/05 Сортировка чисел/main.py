string = input().split()
aux = []

for number in string:
    aux.append(int(number))
aux.sort()
print(*aux, sep=' ')
aux.sort(reverse=True)
print(*aux, sep=' ')
