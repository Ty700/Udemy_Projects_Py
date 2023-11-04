import turtle as t

#Controls:
#   W = Forward
#   A = Turn Counter-clockwise
#   S = Backwards
#   D = Clockwise
#   C = Clear

turt = t.Turtle()

def move_forward():
    turt.forward(10)

def move_backwards():
    turt.backward(10)

def turn_left():
    turt.left(10) 

def turn_right():
    turt.right(10)

def main():
    screen.onkey(key = "w", fun = move_forward)
    screen.onkey(key = "a", fun = turn_left)
    screen.onkey(key = "s", fun = move_backwards)
    screen.onkey(key = "d", fun = turn_right)
    screen.onkey(key = "c", fun = screen.reset)



if __name__ == "__main__":
    t.listen()
    screen = t.Screen()
    main()
    screen.exitonclick()


