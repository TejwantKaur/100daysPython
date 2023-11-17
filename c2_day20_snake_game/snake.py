from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for pos in POSITIONS:
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(pos)
            self.turtles.append(new_turtle)

    def move(self):
        for tur in range(len(self.turtles) - 1, 0, -1):
            # start = 2, stop = 0, steps = -1
            new_x = self.turtles[tur - 1].xcor()
            new_y = self.turtles[tur - 1].ycor()
            self.turtles[tur].goto(new_x, new_y)
        self.turtles[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

