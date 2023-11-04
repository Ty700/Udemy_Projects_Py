from turtle import Turtle

START_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
    def __init__(self) -> None:
        self.snake_segments = []
        self.crete_snake()
        self.head = self.snake_segments[0]
    def crete_snake(self):
        for position in START_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.snake_segments.append(new_segment)

    def move(self):
        for segment_index in range(len(self.snake_segments)-1, 0, -1):
            new_x_pos = self.snake_segments[segment_index - 1].xcor()
            new_y_pos = self.snake_segments[segment_index - 1].ycor()
            self.snake_segments[segment_index].goto(x=new_x_pos, y=new_y_pos)

        self.snake_segments[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if(self.head.heading() != DOWN):
            self.head.setheading(UP)

    def left(self):
        if(self.head.heading() != RIGHT):
            self.head.setheading(LEFT)

    def right(self):
        if(self.head.heading() != LEFT):
            self.head.setheading(RIGHT)

    def down(self):
        if(self.head.heading() != UP):
            self.head.setheading(DOWN)


