str = input()
res = 0
letter = ''

for i in range(len(str)):
    if str[i] == letter:
        res += 1
    letter = str[i]
print(res)
