import turtle
from turtle import *

ALIGNMENT = "center"
FONT = ("courier", 25, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("White")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update()
    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}  ", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.update()
    def inc_score(self):
        self.score+=1

        self.update()
    def lose(self):
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)




