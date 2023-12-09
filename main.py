import time
from turtle import Screen
from player import Player

# from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()

scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Road crossing")

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() > 260:
        player.reset_position()
        scoreboard.point()


screen.exitonclick()
