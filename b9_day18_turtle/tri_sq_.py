from turtle import Turtle, Screen
import random

sc = Screen()
tim = Turtle()


# i = 3
# while i <= 30:
#     angle = 360/i
#     for _ in range(i):
#         tim.forward(50)
#         tim.right(angle)
#     i += 1

colors = [
    "red", "green", "blue", "yellow", "purple",
    "orange", "pink", "brown", "cyan", "lime",
    "teal", "magenta", "black", "gray",
    "lightblue", "darkgreen", "gold", "violet", "turquoise",
]
# line --> kini line draw kerni? tri-->3 , sq-->4 , pen-->5
def draw(lines):
    angle = 360 / lines
    for _ in range(lines):
        tim.forward(50)
        tim.right(angle)

for num in range(3, 20):  # 11 not included 3-->tri, 4-->sq
    tim.color(random.choice(colors))
    draw(num)

sc.exitonclick()
