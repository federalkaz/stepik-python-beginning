string_1 = input().split()
string_2 = input().split()

for i in range(len(string_1)):
    print(int(string_1[i]) + int(string_2[i]), end=' ')
