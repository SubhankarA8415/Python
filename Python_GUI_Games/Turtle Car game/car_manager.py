from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 0


class CarManager(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT
        self.shape('square')
        self.shapesize(1, 2)
        self.penup()
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.goto(pos, random.randint(-240, 240))

    def move(self):
        self.forward(self.car_speed)

    def increase_speed(self):
        global MOVE_INCREMENT
        MOVE_INCREMENT += 10

    def reset(self):
        self.clear()
