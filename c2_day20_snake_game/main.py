from turtle import Screen
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard
import time

sc = Screen()
sc.setup(600, 600)
sc.bgcolor("black")
sc.title("My Snake Game :)")

sc.tracer(0) #to stop animation

snake = Snake()
food = Food()
score = ScoreBoard()

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

    # colision with food
    if(snake.head.distance(food) < 15):
        food.refresh();
        score.inc_score()

    # game_is_on = False


sc.exitonclick()