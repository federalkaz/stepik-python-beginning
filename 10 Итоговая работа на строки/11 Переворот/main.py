string = input()
count, index1, index2 = 0, 0, 0

for i in range(len(string)):
    if string[i] == 'h':
        count += 1
        if count == 1:
            index1 = i
        index2 = i
center = ''
center = string[index1 + 1:index2]
print(string[:index1 + 1] + center[::-1] + string[index2:])
