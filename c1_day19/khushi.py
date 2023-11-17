from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_counterclockwise():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)

def move_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clearscreen():
    tim.clear()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_counterclockwise, "a")
screen.onkey(move_clockwise, "d")
screen.onkey(clearscreen, "c")

screen.exitonclick()