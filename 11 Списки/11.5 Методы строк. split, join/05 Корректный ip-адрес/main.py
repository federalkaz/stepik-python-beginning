strings = input().split('.')

for out in strings:
    if int(out) <= 255:
        continue
    else:
        print('НЕТ')
        exit()
print('ДА')
