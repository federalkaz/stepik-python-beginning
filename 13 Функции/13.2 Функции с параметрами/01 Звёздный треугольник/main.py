def draw_triangle(fill, base):
    aux = base // 2 + 1

    for i in range(1, aux + 1):
        for j in range(1, i + 1):
            print(fill, end='')
        print()

    for i in range(1, base - aux + 1):
        aux -= 1
        for j in range(1, aux + 1):
            print(fill, end='')
        print()


fill = input()
base = int(input())

draw_triangle(fill, base)
