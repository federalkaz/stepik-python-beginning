num = int(input())
last = num % 10
flag = 'YES'

while num > 0:
    aux = num % 10
    if last <= aux:
        last = aux
    else:
        flag = 'NO'
    num = num // 10

print(flag)
