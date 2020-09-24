import turtle

(x, y, distance) = list(map(int, input("Введите через пробел нач. координаты и размер: ").split()))
A = []
with open('commands') as commands:
    for line in commands:
        s = list(map(int, line.rstrip().split(' ')))
        q = []
        for i in range(int(len(s) / 3)):
            q.append((s[3 * i], s[3 * i + 1], s[3 * i + 2]))
        A.append(q)
B = list(map(int, input("Введите через пробел цифры числа: ").split()))
turtle.shape('turtle')
for i in range(len(B)):
    for step_x, step_y, invisible in A[B[i]]:
        if invisible == 1:
            turtle.penup()
        x = x + distance*step_x
        y = y + distance*step_y
        turtle.goto(x, y)
        if invisible == 1:
            turtle.pendown()
