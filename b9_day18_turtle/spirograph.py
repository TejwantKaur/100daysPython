from turtle import Turtle, Screen, colormode
import random

sc = Screen()
tim = Turtle()
colormode(255)
tim.speed("fastest")


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
#     create tuple
    rand_color = (r, g, b)
    return rand_color


def drawGraph(angle):
    wholeAngle = int(360/angle)
    for _ in range(wholeAngle):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + angle)

drawGraph(6)





sc.exitonclick()