from turtle import Turtle, Screen

tim = Turtle()
sc = Screen()

def move_forward():
    tim.forward(10)

def move_back():
    tim.backward(10)

def moveLeft():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def moveRight():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


sc.listen()
sc.onkey(move_forward, "w")
sc.onkey(move_back, "s")
sc.onkey(moveLeft, "a")
sc.onkey(moveRight, "d")
sc.onkey(clear, "c")


sc.exitonclick()