year = int(input())

four = year % 10
three = (year % 100) // 10

if four == 0 and three == 0:
    print('YES')
else:
    print('NO')
