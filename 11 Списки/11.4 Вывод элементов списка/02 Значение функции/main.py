number = int(input())
aux = []

for _ in range(number):
    aux.append(int(input()))
for num in aux:
    print(num)

print('')

for num in aux:
    print(num ** 2 + 2 * num + 1)
