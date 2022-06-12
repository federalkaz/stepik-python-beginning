num = int(input())
total = 0

while num > -1 and num < 6:
    if num == 5:
        total += 1
    num = int(input())

print(total)
