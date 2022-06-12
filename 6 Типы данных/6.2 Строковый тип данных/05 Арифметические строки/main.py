str1, str2, str3 = input(), input(), input()

a, b, c = len(str1), len(str2), len(str3)

if (2 * b - c - a) * (2 * c - b - a) * (2 * a - b - c) == 0:
    print('YES')
else:
    print('NO')
