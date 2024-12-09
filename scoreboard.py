from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.levels = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,260)


    def update_score(self):
        self.clear()
        self.write(f"Level: {self.levels}", align="left", font=FONT)

    def level_up(self):
        self.levels += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)


    pass
