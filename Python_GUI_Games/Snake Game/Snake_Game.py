from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My Snake Game')

screen.tracer(0)  # tracer method will only display when ever we want to make animations smooth

segments = []

snake = Snake()  # creating new snake
food = Food()

f = open('data.txt')
high_score = f.read()
f.close()

scoreboard = Scoreboard(int(high_score))

screen.listen()  # used to listen to keystrokes
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
# screen.update()  # it will display the screen after the above code has been executed
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)  # display will get delay by 1 sec
    # for seg in segments:
    #     seg.forward(20)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset()
        f = open('data.txt', 'w')
        f.write(str(scoreboard.high_score))
        f.close()

    # detect collision with tail
    for segment in snake.segments[1:]:  # except head every other
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            f = open('data.txt', 'w')
            f.write(str(scoreboard.high_score))
            f.close()

screen.exitonclick()
