import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_generate = random.randint(1, 6)
        if random_generate == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            cars_y = random.randint(-250, 250)
            car.goto(x=290, y=cars_y)
            self.cars.append(car)

    def move_cars(self):
        for c in self.cars:
            c.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

