string = input()
flag = 0

for symbol in string:
    if symbol not in '0123456789-':
        flag = 1
if flag == 1:
    print('NO')
else:
    if (string[0:1] == '7' and string[1:2] == "-" and string[5:6] == "-" and string[9:10] == "-") or (string[3:4] == '-' and string[7:8] == '-'):
        print('YES')
    else:
        print('NO')
