a, b, c = int(input()), int(input()), int(input())

if a < b:
    mx = b
    mn = a
else:
    mx = a
    mn = b
if b < c:
    mx = c
else:
    mn = c
if a < c:
    mx = c

print((a + b + c) - (mx + mn))
