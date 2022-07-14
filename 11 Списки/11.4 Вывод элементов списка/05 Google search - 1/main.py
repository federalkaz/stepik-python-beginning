number = int(input())
aux = []
search = ''

for _ in range(number):
    aux.append(input())

search = input()

for string in aux:
    if string.lower().find(search.lower()) != -1:
        print(string)
