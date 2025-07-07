from turtle import Turtle
from typing import List, Any

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):

        self.snake_segs = []
        self.x = -40
        self.create_snake()
        self.head = self.snake_segs[0]

    def create_snake(self):
        self.add_segment((-40,0))
        self.add_segment((-20,0))
        self.add_segment((0,0))






    def add_segment(self,position):
        new_turt = Turtle(shape="square")
        new_turt.penup()
        new_turt.goto(position)
        new_turt.color("White")
        self.snake_segs.append(new_turt)
    def extend(self): # extends snakes tail tend
       self.add_segment(self.snake_segs[-1].position())


    def move(self):

        for segs in range(len(self.snake_segs) - 1, 0, -1):
            new_x = self.snake_segs[segs - 1].xcor()
            new_y = self.snake_segs[segs - 1].ycor()
            self.snake_segs[segs].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def pause(self):
        self.head.forward(0)


