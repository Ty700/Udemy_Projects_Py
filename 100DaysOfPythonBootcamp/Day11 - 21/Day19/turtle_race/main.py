#understanding the screen methods
from turtle import Turtle, Screen
import random

def create_turtles():
    list_of_racers = []

    Donatello = Turtle(shape = "turtle")
    Leonardo = Turtle(shape = "turtle")
    Michelangelo = Turtle(shape = "turtle")
    Raphael = Turtle(shape = "turtle")

    list_of_racers.append(Donatello)
    list_of_racers.append(Leonardo)
    list_of_racers.append(Michelangelo)
    list_of_racers.append(Raphael)

    Raphael.color("red")
    Leonardo.color("blue")
    Donatello.color("purple")
    Michelangelo.color("orange")

    return list_of_racers

def move_to_starting_pos(list_of_turtles):
    x_pos = -225
    y_pos = -150

    for turtle in list_of_turtles:
        turtle.penup()
        turtle.goto(x = x_pos, y = y_pos)
        y_pos += 100

def start_race(list_of_turtles):
    finish_line = 225 #x_pos

    while(True):
        for turtle in list_of_turtles:
            turtle.speed(1)
            currentPos = turtle.position()
            x_pos = currentPos[0]
            # y_pos = currentPos[1]
            if(x_pos >= finish_line):
                return turtle.pencolor()
            else:
                length_to_move = random.randint(1, 5)
                left_and_right_movement = random.randint(-2,2)
                if(left_and_right_movement < 0):
                    turtle.left(abs(left_and_right_movement))
                else:
                    turtle.right(left_and_right_movement)
                turtle.forward(length_to_move)
                

def check_bet(bet, winner):
    print(f"Winner is {winner}!")
    if(bet.lower() == winner.lower()):
        print("You're correct!")
    else:
        print("So close!")

def main(user_bet):
    #creates a list of turtle objs
    racers = create_turtles()
    #moves each turtle to starting pos
    move_to_starting_pos(racers)
    #race starts and winning turtle's color is returned
    winning_turtle = start_race(racers)
    #checks to see if user's guess is the winner
    check_bet(bet = user_bet, winner = winning_turtle)

if __name__ == "__main__":
    #Screen setup
    screen = Screen()
    screen.setup(width = 500, height = 400)

    #Asks which turtles user thinks will win
    user_bet = screen.textinput(title = "Make your bet:", prompt = "Which turtle will win the race? Enter a color (red, blue, purple, orange): ")
    print(f"Let us see if {user_bet} will win the race!")

    main(user_bet)
    
    screen.exitonclick()