from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-200, 250)
        self.level = 1
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 00)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
