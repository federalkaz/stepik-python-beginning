string = input()
total = 0

for i in range(len(string)):
    if string[i] in 'abcdefghijklmnopqrstuvwxyz':
        total += 1

print(total)
