n = int(input())
one, two = 1, 0

for i in range(1, n + 1):
    total = one
    one = total + two
    two = total
    print(total, " ", sep='', end='')
