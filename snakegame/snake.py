from turtle import Turtle

up = 90
left = 180
down = 270
right = 0
positions = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.thesnake = []
        self.create_snake()
        self.snakehead = self.thesnake[0]

    def create_snake(self):
        for snake in positions:
            self.add_snake(snake)

    def add_snake(self, snake):
        snakes = Turtle("square")
        snakes.penup()
        snakes.goto(snake)
        self.thesnake.append(snakes)

    def extend(self):
        self.add_snake(self.thesnake[-1].position())

    def reset(self):
        for snake in self.thesnake:
            snake.goto(1000, 1000)
        self.thesnake.clear()
        self.create_snake()
        self.snakehead = self.thesnake[0]

    def move(self):
        for snake_num in range(len(self.thesnake) - 1, 0, -1):
            new_x = self.thesnake[snake_num - 1].xcor()
            new_y = self.thesnake[snake_num - 1].ycor()
            self.thesnake[snake_num].goto(new_x, new_y)
        self.snakehead.forward(20)

    def up(self):
        if self.snakehead.heading() != down:
            self.snakehead.setheading(up)

    def left(self):
        if self.snakehead.heading() != right:
            self.snakehead.setheading(left)

    def right(self):
        if self.snakehead.heading() != left:
            self.snakehead.setheading(right)

    def down(self):
        if self.snakehead.heading() != up:
            self.snakehead.setheading(down)
