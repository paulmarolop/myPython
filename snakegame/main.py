from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("My Personal SNAKE Game")

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snakehead.distance(food) < 14:
        food.reloc()
        score.score_up()
        snake.extend()

    if snake.snakehead.xcor() > 299 or snake.snakehead.xcor() < -299 or snake.snakehead.ycor() > 299 or snake.snakehead.ycor() < -299:
        score.reset()
        snake.reset()

    for tail in snake.thesnake[1:]:
        if snake.snakehead.distance(tail) < 5:
            score.reset()
            snake.reset()


screen.exitonclick()
