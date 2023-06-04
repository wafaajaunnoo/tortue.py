import turtle
import random

tortue = turtle.Turtle()

tortue.speed('fast')
tortue.shape('turtle')

def carre(longeur):
    cotes = 4
    angle = 90
    for i in range(cotes):
        tortue.forward(longeur)
        tortue.right(angle)

for i in range(10):
    x = random.randint(1, 200)
    y = random.randint(1, 200)
    tortue.goto(x,y)
    carre(100)
