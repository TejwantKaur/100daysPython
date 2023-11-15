from turtle import Turtle, Screen

sc = Screen()
tim = Turtle()

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


sc.exitonclick()