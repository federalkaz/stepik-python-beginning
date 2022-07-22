def print_digit_sum(num):
    list(num)
    res = 0
    for number in num:
        res += int(number)
    print(res)


n = input()

print_digit_sum(n)
