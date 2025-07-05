import turtle
from turtle import Screen
from scoreboard import *
from food import *
from snake import *
import time

screen = Screen()
screen.setup(600, 600)





screen.bgcolor("black")
screen.title("Shnek")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

game_on = True
screen.listen()


screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")


faults = 0

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detects collision with food
    if snake.head.distance(food) < 15:
        food.appear()
        score.update()
        snake.extend()
        score.inc_score()
    #detects collison with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_on = False
        score.lose()
    #detects collision with tail


    for segment in snake.snake_segs[1:]:
        if faults == 2:
            game_on = False
            score.lose()
        elif snake.head.distance(segment) < 10:
            faults+=1


screen.mainloop()
