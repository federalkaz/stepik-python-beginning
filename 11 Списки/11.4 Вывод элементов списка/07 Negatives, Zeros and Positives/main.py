number = int(input())
negatives, zeros, positives = [], [], []

for _ in range(number):
    n = int(input())
    if n < 0:
        negatives.append(n)
    elif n == 0:
        zeros.append(n)
    else:
        positives.append(n)

for str1 in negatives:
    print(str1)
for str2 in zeros:
    print(str2)
for str3 in positives:
    print(str3)
