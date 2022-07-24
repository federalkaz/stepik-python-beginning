words = input().split()

print(*[words[i][1:] + words[i][0:1] + 'ки' for i in range(len(words))])
