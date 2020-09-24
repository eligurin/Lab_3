import turtle

(x, y, distance) = list(map(int, input("Введите через пробел нач. координаты и размер: ").split()))
zero = [(0, 2, 0), (1, 0, 0), (0, -2, 0), (-1, 0, 0), (2, 0, 1)]
one = [(0, 1, 1), (1, 1, 0), (0, -2, 0), (1, 0, 1)]
two = [(0, 2, 1), (1, 0, 0), (0, -1, 0), (-1, -1, 0), (1, 0, 0), (1, 0, 1)]
three = [(1, 1, 0), (-1, 0, 0), (1, 1, 0), (-1, 0, 0), (2, -2, 1)]
four = [(0, 2, 1), (0, -1, 0), (1, 0, 0), (0, 1, 1), (0, -2, 0), (1, 0, 1)]
five = [(1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, 1, 0), (1, 0, 0), (1, -2, 1)]
six = [(1, 2, 1), (-1, -1, 0), (0, -1, 0), (1, 0, 0), (0, 1, 0), (-1, 0, 0), (2, -1, 1)]
seven = [(0, 1, 0), (1, 1, 0), (-1, 0, 0), (2, -2, 1)]
eight = [(0, 2, 0), (1, 0, 0), (0, -2, 0), (-1, 0, 0), (0, 1, 1), (1, 0, 0), (1, -1, 1)]
nine = [(1, 1, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0), (1, 0, 0), (1, -1, 1)]
A = [zero, one, two, three, four, five, six, seven, eight, nine]
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
