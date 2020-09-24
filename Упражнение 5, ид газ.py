import turtle
import numpy
from random import randint

(number_of_turtles, steps_of_time_number, length) = list(map(int, input().split()))
step_length = float(input())

turtle.penup()
turtle.goto(-length/2, -length/2)
turtle.pendown()
for i in range(4):
    turtle.forward(length)
    turtle.left(90)
turtle.hideturtle()

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
angle = [randint(-180, 180) for i in range(number_of_turtles)]
dx = [step_length * numpy.cos(angle[i]) for i in range(number_of_turtles)]
dy = [step_length * numpy.sin(angle[i]) for i in range(number_of_turtles)]
x = [randint(-length/2, length/2) for i in range(number_of_turtles)]
y = [randint(-length/2, length/2) for i in range(number_of_turtles)]

for i in range(number_of_turtles):
    pool[i].penup()
    pool[i].speed(50)
    pool[i].goto(x[i], y[i])

for i in range(steps_of_time_number):
    for k in range(number_of_turtles):
        x[k] += dx[k]
        y[k] += dy[k]
        pool[k].goto(x[k], y[k])
        if pool[k].xcor() > length/2 - step_length or pool[k].xcor() < -length/2 + step_length:
            dx[k] = -dx[k]
        if pool[k].ycor() > length/2 - step_length or pool[k].ycor() < -length/2 + step_length:
            dy[k] = -dy[k]
