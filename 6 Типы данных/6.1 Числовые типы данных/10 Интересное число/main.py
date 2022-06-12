num = int(input())

one = num // 100
two = num // 10 % 10
three = num % 10

maximum = max(one, two, three)
minimal = min(one, two, three)
average = (one + two + three) - (maximum + minimal)

if (maximum - minimal) == average:
    print("Число интересное")
else:
    print("Число неинтересное")
