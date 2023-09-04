from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('#EADBC8')
screen.title("Snake Game by Lakshmi...")
screen.tracer(0)

food = Food()
snake = Snake()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with the wall
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -299 or \
       snake.segments[0].ycor() > 298 or snake.segments[0].ycor() < -298:
        scoreboard.reset()
        snake.reset()
        food.refresh()

    # Detect collision with tail
    for segments in snake.segments[1:]:
        if segments == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segments) < 10:
            scoreboard.reset()
            snake.reset()
            food.refresh()


screen.exitonclick()
