import turtle as t
import random

def get_random_pen_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    return new_color

def draw_spirograph(turtle, resolution):
    for _ in range(resolution):
        turtle.pencolor(get_random_pen_color())
        turtle.circle(100)
        turtle.left(360 / resolution)

def main():
    t.colormode(255)
    turt = t.Turtle()
    turt.speed(0)
    turt.pensize(1)
    draw_spirograph(turt, 72)

if __name__ == "__main__":
    main()
    screen = t.Screen()
    screen.exitonclick()