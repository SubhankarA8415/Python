from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
