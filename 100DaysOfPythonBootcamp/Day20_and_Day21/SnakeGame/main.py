from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from turtle import Screen
import time

X_BOUNDARY = 295
Y_BOUNDARY = 295

def configure_screen():
    screen = Screen()
    screen.setup(height=600,width=600)
    screen
    screen.bgcolor("black")
    screen.tracer(0)
    screen.listen()
    return screen

def snake_hit_wall(snake):
        if(snake.head.xcor() > X_BOUNDARY or snake.head.xcor() < -X_BOUNDARY #x left or x Right
           or snake.head.ycor() > Y_BOUNDARY or snake.head.ycor() < -Y_BOUNDARY): #y up or y down
            return True
        else:
             return False   

def main():
    screen = configure_screen()
    snake = Snake() 
    food = Food()
    score_board = ScoreBoard()

    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)
    screen.onkey(key="Down", fun=snake.down) 

    game_is_on = True
    while(game_is_on): 
        screen.update()
        time.sleep(0.1)
        snake.move()

        #snake has collided with the food
        if(snake.head.distance(food) <= 15):
            #move food
            food.refresh_food_location()
            #adds new segment
            snake.extend()
            #increase score 
            score_board.increase_score()
        
        #detect collision with wall
        if(snake_hit_wall(snake)):
            game_is_on = False
            score_board.game_over()

        #Detect Collision with tail
        #Skips head. snake_segments[0] = head
        for segment in snake.snake_segments[1:]:
            if(snake.head.distance(segment) < 10):
                game_is_on = False
                score_board.game_over()

    screen.exitonclick()
if __name__ == "__main__":
    main()
    