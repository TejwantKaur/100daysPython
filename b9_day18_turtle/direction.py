from turtle import Turtle, Screen, colormode
import random

sc = Screen()
tim = Turtle()
colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
#     create tuple
    rand_color = (r, g, b)
    return rand_color

# colors = [
#     "red", "green", "blue", "yellow", "purple",
#     "orange", "pink", "brown", "cyan", "lime",
#     "teal", "magenta", "black", "gray",
#     "lightblue", "darkgreen", "gold", "violet", "turquoise",
# ]


direction = [0, 90, 180, 270]
tim.pensize(7)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(20)
    tim.setheading(random.choice(direction))


















sc.exitonclick()