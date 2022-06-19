num = int(input())
string = input()
res = ''

for i in range(len(string)):
    aux = ord(string[i]) - num
    if aux < 97:
        aux += 26
    res += chr(aux)

print(res)
