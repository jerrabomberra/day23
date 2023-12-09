from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.showturtle()
        self.speed(1)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(0, new_y)

    def reset_position(self):
        self.goto(STARTING_POSITION)
