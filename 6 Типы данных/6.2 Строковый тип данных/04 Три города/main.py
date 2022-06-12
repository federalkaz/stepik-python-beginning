city1, city2, city3 = input(), input(), input()

if len(city1) >= len(city2):
    max = city1
    if len(city1) >= len(city3):
        max = city1
    else:
        max = city3
else:
    max = city2
    if len(city2) >= len(city3):
        max = city2
    else:
        max = city3

if len(city1) <= len(city2):
    min = city1
    if len(city1) <= len(city3):
        min = city1
    else:
        min = city3
else:
    min = city2
    if len(city2) <= len(city3):
        min = city2
    else:
        min = city3

print(min, max, sep='\n')
