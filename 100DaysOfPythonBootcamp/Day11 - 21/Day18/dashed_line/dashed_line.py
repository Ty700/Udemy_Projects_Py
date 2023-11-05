import turtle as t

def make_square():
    for _ in range(4):
        make_dashed_line(10)
        turt.left(90)

def make_dashed_line(length):
    for _ in range(10):
        turt.pendown()
        turt.forward(length)
        turt.penup()
        turt.forward(length)


turt = t.Turtle()

def main():
    make_square()

if __name__ == "__main__":
    main()
    screen = t.Screen()
    screen.exitonclick()




