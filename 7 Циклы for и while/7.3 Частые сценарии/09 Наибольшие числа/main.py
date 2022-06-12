n = int(input())
big1, big2 = 0, 0

for i in range(n):
    num = int(input())
    if num > big1:
        big2 = big1
        big1 = num
    elif num > big2:
        big2 = num

print(big1, big2, sep='\n')
