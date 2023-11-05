from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("gold")
        self.speed("fastest")
        self.refresh_food_location()

    def refresh_food_location(self):
        new_xpos = random.randint(-275, 275)
        new_ypos = random.randint(-275, 275)

        while(new_xpos % 5 != 0):
            new_xpos = random.randint(-275, 275)

        while(new_ypos % 20 != 0):
            new_ypos = random.randint(-275, 275)
        
        return self.goto(new_xpos, new_ypos)