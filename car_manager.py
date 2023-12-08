from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

cars = {}


class CarManager(Turtle):
    def __init__(self):
        super().__init__
        self.color = random.choice(COLORS)
        for idx, color in enumerate(COLORS):
            cars[idx] = color


car = CarManager()

print(cars)
# print(car.color)
# number of cars
# vertical position of cars (ycord())
# car size
# random starting position
# speed increases after score increases
