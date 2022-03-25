num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
num_4 = int(input())
# по вертикали - номер столбца такой же (равен), номер строки меньше или больше на 1
# по горизонтали - номер столбца больше или меньше на 1, номер строки такой же (равен)
if (num_1 == num_3) and (num_2 != num_4) or ((num_1 - num_3) and (num_2 == num_4)):
    print('YES')
else:
    print('NO')
