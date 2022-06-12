a_1, b_1, a_2, b_2 = int(input()), int(input()), int(input()), int(input())

if a_1 <= b_1 < a_2 <= b_2 or a_2 <= b_2 < a_1 <= b_1:
    print('пустое множество')
elif a_1 < a_2:
    if b_1 == a_2:
        print(a_2)
    elif b_1 > b_2:
        print(a_2, b_2)
    elif b_1 == b_2:
        print(a_2, b_2)
    elif b_1 < b_2:
        print(a_2, b_1)
elif a_1 > a_2:
    if b_2 == a_1:
        print(a_1)
    elif b_2 > b_1:
        print(a_1, b_1)
    elif b_1 == b_2:
        print(a_1, b_1)
    elif b_2 < b_1:
        print(a_1, b_2)
elif a_1 == a_2:
    if b_2 > b_1:
        print(a_1, b_1)
    elif b_1 == b_2:
        print(a_1, b_1)
    elif b_1 > b_2:
        print(a_2, b_2)
