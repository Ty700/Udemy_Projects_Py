from turtle import Turtle, Screen

turt = Turtle()
screen = Screen()

def move_forwards():
    turt.forward(10)

screen.listen()
screen.onkey(key = "w", fun = move_forwards)
screen.exitonclick()