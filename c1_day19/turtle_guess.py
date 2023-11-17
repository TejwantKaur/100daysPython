from turtle import Turtle, Screen
import random

sc = Screen()
sc.setup(width=500, height=400)
# user_bet = sc.textinput(title="Make your bet: ", prompt="Which turtle will win the race? ")
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_pos = [-70, -40, -10, 20, 50, 80, 110]

is_race_on = False;
user_bet = sc.textinput(title="Make your bet", prompt = "Which turtle will win the race!?\n Enter color: ")
all_turtles = []

for idx in range(0, 7):
    tim = Turtle("turtle")
    tim.penup()
    tim.color(colors[idx])
    tim.goto(x=-230, y=y_pos[idx])
    all_turtles.append(tim)


if user_bet:
    is_race_on = True;

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False;
            winning_clr = turtle.pencolor()
            if winning_clr == user_bet:
                print(f"You've won! The {winning_clr} turtle is the winner.. :)")
            else:
                print(f"You've lost! The {winning_clr} turtle is the winner.. :)")

        rand_dis = random.randint(0, 10)
        turtle.forward(rand_dis)

sc.exitonclick()