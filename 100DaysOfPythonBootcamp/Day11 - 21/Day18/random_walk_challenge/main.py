import turtle as t
import colors
import random

def get_random_pen_color():
    # return random.choice(colors.list_of_colors)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

def get_random_direction():
    directions = [0, 90, 180, 270]
    return random.choice(directions)

def random_walk(turtle):
    turtle.speed(10)
    for i in range(100):
        turtle.pencolor(get_random_pen_color())
        turtle.seth(get_random_direction())
        turtle.forward(20)        

def get_random_walk_length():
    return random.randint(10, 50)

# def main():
 
#     turt = t.Turtle()
#     turt2 = t.Turtle()
#     turt3 = t.Turtle()

#     turt.pensize(5)
#     turt2.pensize(5)
#     turt3.pensize(5)

#     turt.speed(10)
#     turt2.speed(10)
#     turt3.speed(10)

#     for _ in range(1000):
#         color = get_random_pen_color()
#         color2 = get_random_pen_color()
#         color3 = get_random_pen_color()
        
#         turt.pencolor(color)
#         turt2.pencolor(color2)
#         turt3.pencolor(color3)

#         turt.seth(get_random_direction())
#         turt2.seth(get_random_direction())
#         turt3.seth(get_random_direction())



#         turt.forward(get_random_walk_length())
#         turt2.forward(get_random_walk_length())
#         turt3.forward(get_random_walk_length())

def main():
    t.colormode(255)
    turt = t.Turtle()
    turt.pensize(5)
    random_walk(turt)



if __name__ == "__main__":
    main()
    screen = t.Screen()
    screen.exitonclick()
       