str = input()
plus, zvezda = 0, 0


for i in range(len(str)):
    if str[i] in '+':
        plus += 1
    if str[i] in '*':
        zvezda += 1

print("Символ + встречается", plus, "раз")
print("Символ * встречается", zvezda, "раз")
