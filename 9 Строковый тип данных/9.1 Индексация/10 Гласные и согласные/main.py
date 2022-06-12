str = input()
glas, soglas = 0, 0

for i in range(len(str)):
    if str[i] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        glas += 1
    if str[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        soglas += 1

print("Количество гласных букв равно", glas)
print("Количество согласных букв равно", soglas)
