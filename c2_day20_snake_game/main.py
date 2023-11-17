from turtle import Screen, Turtle
import time
from snake import Snake

sc = Screen()
sc.setup(600, 600)
sc.bgcolor("black")
sc.title("My Snake Game :)")

sc.tracer(0) #to stop animation

snake = Snake()

sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    sc.update()  # refresh the screen
    time.sleep(0.1) # piece by piece, ik pice move krega next 0.1 sec bad agla usto 0.1 sec bad
    snake.move()

    # game_is_on = False


sc.exitonclick()