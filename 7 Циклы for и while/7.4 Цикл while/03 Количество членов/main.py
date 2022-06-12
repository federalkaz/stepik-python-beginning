str = input()
i = 0

while (str != 'стоп') and (str != 'хватит') and (str != 'достаточно'):
    i += 1
    str = input()

print(i)