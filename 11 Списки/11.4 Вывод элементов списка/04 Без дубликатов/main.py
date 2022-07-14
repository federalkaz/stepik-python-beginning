number = int(input())
aux = []
string = ''

for _ in range(number):
    string = input()
    if string not in aux:
        aux.append(string)

for num in aux:
    print(num, end='\n')
