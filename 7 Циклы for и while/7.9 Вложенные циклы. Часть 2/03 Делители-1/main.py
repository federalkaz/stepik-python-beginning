num1, num2 = int(input()), int(input())
sum_del, max_num = 0, 0

for i in range(num1, num2 + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += j
        if count >= sum_del:
            sum_del = count
            max_num = i
print(max_num, sum_del)
