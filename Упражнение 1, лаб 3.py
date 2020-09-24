import turtle
from random import *

n = int(input())
turtle.shape('turtle')
for i in range(1, n+1, 1):
    turtle.forward(randint(5, 50))
    turtle.left(randint(-180, 180))
