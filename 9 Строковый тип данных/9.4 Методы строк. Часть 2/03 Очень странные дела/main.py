num = int(input())
total = 0

for _ in range(num):
    string = input()
    if string.count('11') > 2:
        total += 1

print(total)
