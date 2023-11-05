from turtle import Turtle

TITLE_ALIGHTMENT = "center"
FONT = ("Arial", 20, "bold")

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.pencolor("White")
        self.goto(0,270)
        self.update_title()

    def update_title(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=TITLE_ALIGHTMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_title()
    
    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER.", move=False, align=TITLE_ALIGHTMENT, font=FONT)