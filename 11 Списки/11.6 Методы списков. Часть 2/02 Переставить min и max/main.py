string = input().split()
max, min = 0, 99

for number in string:
    if int(number) > max:
        max = int(number)
    if int(number) < min:
        min = int(number)

index_min = string.index(str(min))
index_max = string.index(str(max))

string[index_min], string[index_max] = string[index_max], string[index_min]

for out in string:
    print(out, end=' ')
