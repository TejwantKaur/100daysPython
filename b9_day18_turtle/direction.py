from turtle import Turtle, Screen
import random

sc = Screen()
tim = Turtle()

colors = [
    "red", "green", "blue", "yellow", "purple",
    "orange", "pink", "brown", "cyan", "lime",
    "teal", "magenta", "black", "gray",
    "lightblue", "darkgreen", "gold", "violet", "turquoise",
]

direction = [0, 90, 180, 270]
tim.pensize(7)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(20)
    tim.setheading(random.choice(direction))


















sc.exitonclick()