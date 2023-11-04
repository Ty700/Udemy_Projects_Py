from snake import Snake
from turtle import Screen
import time

def configure_screen():
    screen = Screen()
    screen.setup(height=600,width=600)
    screen.bgcolor("black")
    screen.tracer(0)
    screen.listen()
    return screen

def main():
    screen = configure_screen()

    snake = Snake() 

    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)
    screen.onkey(key="Down", fun=snake.down) 

    game_is_on = True
    while(game_is_on): 

        screen.update()
        time.sleep(0.1)
        snake.move()

    screen.exitonclick()
if __name__ == "__main__":
    main()
    