flag = 1

for _ in range(10):
    num = int(input())
    if num % 2 != 0:
        flag = 0

if flag == 0:
    print('NO')
else:
    print('YES')
