strings = []

for _ in range(int(input().lstrip('#'))):
    strings.append(input())

for string in strings:
    num = len(string)
    if '#' in string:
        num = string.index('#')
    print(string[:num].rstrip())
