import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')

player = Player()
car = CarManager(320)
scoreboard = Scoreboard()
cars = []

screen.listen()
screen.onkeypress(player.move_up, 'Up')
screen.onkeypress(player.move_down, 'Down')

carCreate = 0

while carCreate < 100:
    pos = random.randint(-300, 300)
    if carCreate % 8 == 0:
        car = CarManager(pos)
        cars.append(car)
    carCreate += 1

carCreate = 0
game_is_on = True
while game_is_on:

    time.sleep(0.1)

    if carCreate % 8 == 0:
        car = CarManager(320)
        cars.append(car)

    for car in cars:
        car.move()

    carCreate += 1

    for car in cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 270:
        car.increase_speed()
        scoreboard.increase_level()
        player.reset()

    screen.update()

screen.exitonclick()
