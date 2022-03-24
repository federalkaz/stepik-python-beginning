num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
num_4 = int(input())

if num_1 < num_2:
    res_1 = num_1
else:
    res_1 = num_2
if num_3 < num_4:
    res_2 = num_3
else:
    res_2 = num_4
if res_1 < res_2:
    print(res_1)
else:
    print(res_2)
