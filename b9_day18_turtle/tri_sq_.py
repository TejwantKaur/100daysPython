from turtle import Turtle, Screen

sc = Screen()
tim = Turtle()


# i = 3
# while i <= 30:
#     angle = 360/i
#     for _ in range(i):
#         tim.forward(50)
#         tim.right(angle)
#     i += 1

# line --> kini line draw kerni? tri-->3 , sq-->4 , pen-->5
def draw(lines):
    angle = 360 / lines
    for _ in range(lines):
        tim.forward(50)
        tim.right(angle)


for num in range(3, 15):  # 11 not included 3-->tri, 4-->sq
    draw(num)

sc.exitonclick()
