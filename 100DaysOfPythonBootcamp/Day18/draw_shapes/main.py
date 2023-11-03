import turtle as t
import random
from colors import colors

def random_color():
    return random.choice(colors)

def draw_shapes(turtle):
    for currentSides in range(3, 11):
        turtle.pencolor(random_color())
        currentAngle = 360 / currentSides
        for _ in range(currentSides):
            turtle.left(currentAngle)
            turtle.forward(100)
        
        currentSides += 1
        

def main():
    turt = t.Turtle()
    turt.penup()
    turt.sety(-650)
    turt.pendown()
    draw_shapes(turt)



if __name__ == "__main__":
    main()
    screen = t.Screen()
    screen.exitonclick()