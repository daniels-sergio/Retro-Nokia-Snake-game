import turtle
from turtle import *

ALIGNMENT = "center"
FONT = ("courier", 25, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update()
    def update(self):
        self.write(f"Score: {self.score}  ", align=ALIGNMENT, font=FONT)

    def inc_score(self):
        self.score+=1
        self.clear()
        self.update()
    def lose(self):
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

#list = [1,2,3,4,5,6,7,8,9,10]


#for i in list[3:100]:
    #print(i)



