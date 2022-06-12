num = int(input())
aux = num % 10
flag = 'YES'

while num > 0:
    if aux != num % 10:
        flag = 'NO'
    num = num // 10

print(flag)
