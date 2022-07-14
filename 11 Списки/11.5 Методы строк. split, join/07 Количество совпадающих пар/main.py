string = input().split()
res = 0

for i in range(len(string)):
    for j in range(i + 1, len(string)):
        if string[i] == string[j]:
            res += 1

print(res)
