num = int(input())

if num == 0:
    print('зеленый')
elif 0 < num < 11 and num % 2 > 0:
    print('красный')
elif 0 < num < 11 and num % 2 == 0:
    print('черный')
elif 10 < num < 19 and num % 2 > 0:
    print('черный')
elif 10 < num < 19 and num % 2 == 0:
    print('красный')
elif 18 < num < 29 and num % 2 > 0:
    print('красный')
elif 18 < num < 29 and num % 2 == 0:
    print('черный')
elif 28 < num < 37 and num % 2 > 0:
    print('черный')
elif 28 < num < 37 and num % 2 == 0:
    print('красный')
else:
    print('ошибка ввода')
