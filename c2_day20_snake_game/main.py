from turtle import Screen
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard
import time

sc = Screen()
sc.setup(600, 600)
sc.bgcolor("black")
sc.title("My Snake Game :)")

sc.tracer(0)  # to stop animation

snake_obj = Snake()
food_obj = Food()
scoreboard_obj = ScoreBoard()

sc.listen()
sc.onkey(snake_obj.up, "Up")
sc.onkey(snake_obj.down, "Down")
sc.onkey(snake_obj.left, "Left")
sc.onkey(snake_obj.right, "Right")

game_is_on = True
while game_is_on:
    sc.update()  # refresh the screen
    time.sleep(0.1)  # piece by piece, ik pice move krega next 0.1 sec bad agla usto 0.1 sec bad
    snake_obj.move()

    # colision with food
    if snake_obj.head.distance(food_obj) < 15:
        food_obj.refresh();
        snake_obj.extend_snake()
        scoreboard_obj.inc_score()

    # 20 - width of snake
    # collision with wall
    if (snake_obj.head.xcor() > 290 or snake_obj.head.xcor() < -280 or snake_obj.head.ycor() > 290 or snake_obj.head.ycor() < -280):
        game_is_on = False
        scoreboard_obj.game_over()

#   detecting collision with tail
    for tur in snake_obj.turtles:
        if tur == snake_obj.head:
            pass
        elif snake_obj.head.distance(tur) < 10:
            game_is_on = False
            scoreboard_obj.game_over()

sc.exitonclick()
