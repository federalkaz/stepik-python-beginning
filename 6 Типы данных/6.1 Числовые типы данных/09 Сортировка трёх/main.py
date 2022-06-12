num1 = int(input())
num2 = int(input())
num3 = int(input())

one = max(num1, num2, num3)
three = min(num1, num2, num3)
two = (num1 + num2 + num3) - (one + three)

print(one)
print(two)
print(three)
