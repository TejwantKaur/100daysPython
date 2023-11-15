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
    color = (r, g, b)
    return color

tim.speed("fastest")
tim.circle(100)

def drawGraph(angle):
    for _ in range(100):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + 5)



sc.exitonclick()