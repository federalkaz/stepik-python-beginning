number = int(input())

print([i * 2 for i in range(1, number) if (i * 2) % 2 == 0 and (i * 2) <= number])
