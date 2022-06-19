string = input()
total = 0

for i in range(len(string)):
    if string[i] in '1234567890':
        total += 1

print(total)
