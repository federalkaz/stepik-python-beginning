str = input()
one, two = '', ''

if len(str) % 2 > 0:
    one = str[:len(str) // 2 + 1]
    two = str[len(str) // 2 + 1:]
else:
    one = str[:len(str) // 2]
    two = str[len(str) // 2:]

print(two + one)
