num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
num_4 = int(input())

if num_1 == num_3 and abs(num_2 - num_4) == 1 or abs(num_1 - num_3) == 1 and num_2 == num_4 or abs(num_1 - num_3) == 1 and abs(num_2 - num_4) == 1:
    print('YES')
else:
    print('NO')
