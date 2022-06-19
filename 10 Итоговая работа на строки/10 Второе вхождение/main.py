string = input()
count, index = 0, 0

for i in range(len(string)):
    if string[i] == 'f':
        count += 1
        if count == 2:
            index = i
            break
if count == 1:
    print(-1)
if count == 2:
    print(index)
if count == 0:
    print(-2)
