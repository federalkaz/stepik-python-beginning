number = int(input())
aux = []

for _ in range(number):
    aux.append(int(input()))

aux.remove(max(aux))
aux.remove(min(aux))

for num in aux:
    print(num, end='\n')
