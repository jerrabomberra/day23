STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.goto(STARTING_POSITION)
        self.y_move = 3
        self.move_speed = 1

    def move(self):
        self.
        


        