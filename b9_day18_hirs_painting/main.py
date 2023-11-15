# import colorgram
import random
# Extract 6 colors from an image.
# colors = colorgram.extract("image.jpg", 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

from turtle import Turtle, Screen, colormode

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
              (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = Turtle()
sc = Screen()
colormode(255)

tim.penup()
tim.setheading(225) # angle
tim.forward(315)
tim.setheading(0)
tim.speed("fastest")

numofdots = 100


def upline():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(50 * 10)
    tim.setheading(0)


for dots in range(1, numofdots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dots % 10 == 0:
        upline()


# for _ in range(15):
#     for _ in range(16):
#         tim.dot(20, random.choice(color_list)) #--> radius = 20
#         # tim.penup()
#         tim.forward(30)
#         # tim.pendown()
#     upline()


















sc.exitonclick()