weight = int(input())

if weight < 60:
    print('Легкий вес')
elif 59 < weight < 64:
    print('Первый полусредний вес')
else:
    print('Полусредний вес')
