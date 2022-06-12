stolbec1 = int(input())
stroka1 = int(input())
stolbec2 = int(input())
stroka2 = int(input())


if ((stolbec1 % 2 > 0) and (stroka1 % 2 > 0)) or ((stolbec1 % 2 == 0) and (stroka1 % 2 == 0)) and ((stolbec2 % 2 > 0) and (stroka2 % 2 > 0)) or ((stolbec2 % 2 == 0) and (stroka2 % 2 == 0)):
    print('YES')
if ((stolbec1 % 2 > 0) and (stroka1 % 2 == 0)) or ((stolbec1 % 2 == 0) and (stroka1 % 2 > 0)) and ((stolbec2 % 2 > 0) and (stroka2 % 2 == 0)) or ((stolbec2 % 2 == 0) and (stroka2 % 2 > 0)):
    print('NO')

# Решение:
if (stolbec1 + stroka1 + stolbec2 + stroka2) % 2 == 0:
    print('YES')
else:
    print('NO')

