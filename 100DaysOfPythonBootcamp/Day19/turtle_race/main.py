#understanding the screen methods

from turtle import Turtle, Screen
import random

def move_to_starting_pos(list_of_turtles):
    x_pos = -225
    y_pos = -150

    for turtle in list_of_turtles:
        turtle.penup()
        turtle.goto(x_pos, y_pos)
        y_pos += 100

def start_race(list_of_turtles):
    while(True):
        for turtle in list_of_turtles:
            turtle.speed(1)

            currentPos = turtle.position()
            x_pos = currentPos[0]
            # y_pos = currentPos[1]
            if(x_pos >= 225):
                return turtle.color()
            else:
                length_to_move = random.randint(1, 5)
                turtle.forward(length_to_move)

def main(user_bet):
    racers = []

    Donatello = Turtle(shape = "turtle")
    Leonardo = Turtle(shape = "turtle")
    Michelangelo = Turtle(shape = "turtle")
    Raphael = Turtle(shape = "turtle")

    racers.append(Donatello)
    racers.append(Leonardo)
    racers.append(Michelangelo)
    racers.append(Raphael)

    Raphael.color("red")
    Leonardo.color("blue")
    Donatello.color("purple")
    Michelangelo.color("orange")

    move_to_starting_pos(racers)
    # winner = start_race(racers)
    # print(f"Winner is {winner.color}")
    


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width = 500, height = 400)
    user_bet = screen.textinput(title = "Make your bet:", prompt = "Which turtle will win the race? Enter a color (red, blue, purple, orange): ")

    main(user_bet)
    
    screen.exitonclick()