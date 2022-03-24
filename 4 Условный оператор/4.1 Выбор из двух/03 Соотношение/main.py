number = int(input())
four = number % 10
three = (number % 100) // 10
two = (number// 100) % 10
one = number // 1000
if (one + four) == (two - three):
    print('ДА')
else:
    print('НЕТ')
