string = input()
res = ''
max = 0

for i in range(len(string)):
    if max <= string.count(string[i]):
        max = string.count(string[i])
        res = string[i]

print(res)
