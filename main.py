from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

print("s: down, a: left, d: right, w: up")

snake = Snake()
screen = Screen()
food = Food()
scoreboard = Scoreboard()

screen.setup(600, 600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)
screen.update()
screen.listen()
screen.onkey(fun=snake.turn_up, key="w")
screen.onkey(fun=snake.turn_left, key="a")
screen.onkey(fun=snake.turn_down, key="s")
screen.onkey(fun=snake.turn_right, key="d")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    ## Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    ## Detect collision with wall
    if (snake.head.xcor() > 295
            or snake.head.xcor() < -295) or (snake.head.ycor() > 295
                                             or snake.head.ycor() < -295):
        scoreboard.reset()
        scoreboard.game_over()
        game_is_on = False

    ## Detect Collision with tail
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            scoreboard.game_over()
            game_is_on = False
