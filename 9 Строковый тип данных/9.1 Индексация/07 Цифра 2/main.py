str = input()
flag = 0

for i in range(len(str)):
    if str[i] in '0123456789':
        flag = 1
if flag == 1:
    print('Цифра')
else:
    print('Цифр нет')
