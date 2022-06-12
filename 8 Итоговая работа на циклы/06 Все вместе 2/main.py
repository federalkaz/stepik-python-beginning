num = int(input())
one_task, two_task, three_task, four_task, five_task, six_task = 0, 0, 0, 0, 1, 0

aux1 = num
while aux1 > 0:
    if aux1 % 10 == 3:
        one_task += 1
    aux1 //= 10
print(one_task)

aux2 = num
last_digit = aux2 % 10
while aux2 > 0:
    if aux2 % 10 == last_digit:
        two_task += 1
    aux2 //= 10
print(two_task)

aux3 = num
while aux3 > 0:
    if ((aux3 % 10) % 2 == 0):
        three_task += 1
    aux3 //= 10
print(three_task)

aux4 = num
while aux4 > 0:
    if ((aux4 % 10) > 5):
        four_task += aux4 % 10
    aux4 //= 10
print(four_task)

aux5 = num
while aux5 > 0:
    if ((aux5 % 10) > 7):
        five_task *= aux5 % 10
    aux5 //= 10
if (five_task == 0):
    print(1)
else:
    print(five_task)

aux6 = num
while aux6 > 0:
    if aux6 % 10 == 0 or aux6 % 10 == 5:
        six_task += 1
    aux6 //= 10
print(six_task)
