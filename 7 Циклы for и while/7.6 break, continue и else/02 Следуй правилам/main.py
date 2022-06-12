n = int(input())
i = 0
while i < n:
    i += 1
    if 4 < i < 10:
        continue
    if 16 < i < 38:
        continue
    if 77 < i < 88:
        continue
    print(i)
