from turtle import Turtle, Screen

sc = Screen()
tim = Turtle()

i = 3
while i <= 30:
    angle = 360/i
    for _ in range(i):
        tim.forward(50)
        tim.right(angle)
    i += 1













sc.exitonclick()