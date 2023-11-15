from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.color("DeepSkyBlue")

# i = 0
# while i < 4:
#     timmy.forward(100)
#     timmy.right(90)
#     i += 1

for _ in range(4):
    timmy.forward(100)
    timmy.left(90)

screen = Screen()
screen.exitonclick()



