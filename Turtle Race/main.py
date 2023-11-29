from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Your Bet", prompt="Which turtle you bet win the race ? ")
colors = ["red", "blue", "yellow", "purple", "green", "orange"]
y_position = [-100, -60, -20, 20, 60, 100]
all_turtles = []
race_on = False

for turtles in range(0, 6):
    the_turtle = Turtle("turtle")
    the_turtle.penup()
    the_turtle.color(colors[turtles])
    the_turtle.goto(x=-240, y=y_position[turtles])
    all_turtles.append(the_turtle)


if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 240:
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print("You Win")
                race_on = False
            else:
                print(f"You lose, the winner is {winner_color} turtle")
                race_on = False
        rand_speed = random.randint(1, 10)
        turtle.forward(rand_speed)


screen.exitonclick()
