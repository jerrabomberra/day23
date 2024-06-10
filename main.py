import time
from turtle import Screen
from player import Player
from car_manager import CarManager

# from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()

scoreboard = Scoreboard()

car_manager = CarManager()

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
    car_manager.create_car()
    car_manager.move_cars()

    if player.is_at_finish_line():
        player.reset_position()
        car_manager.level_up()
        scoreboard.increase_level()

    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
