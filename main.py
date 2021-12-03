from turtle import Screen

from food import Food
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)  # using keyword arguments
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
# TODO: 1) Create a snake body
# when we create a turtle object. It is 20 x 20 pixels in dimension.
# Master branch contains Angela's code, my-work branch contains my code.
snake = Snake()
food = Food()
# TODO: 3) Control the snake
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # It is basically controlling the screen refresh rate. The sooner screen updates/Refresh, the
    # the faster snake appears to move.
    # TODO: 2) Move the snake
    snake.move()

screen.exitonclick()
