num = int(input())

if (((10000 > num) and (num > 999)) and (((num % 7) == 0) or ((num % 17) == 0))):
    print('YES')
else:
    print('NO')
