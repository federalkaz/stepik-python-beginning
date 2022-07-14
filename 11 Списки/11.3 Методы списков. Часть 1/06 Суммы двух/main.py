num = int(input())
res1, res2 = [], []

for _ in range(1, num + 1):
    res1.append(int(input()))
for i in range(0, num - 1):
    res2.append(res1[i] + res1[i + 1])

print(res2)
