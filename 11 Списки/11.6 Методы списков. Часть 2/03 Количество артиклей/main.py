string = input().lower().split(' ')
count = 0

for word in string:
    if word in ['a', 'an', 'the']:
        count += 1

print('Общее количество артиклей:', count)
