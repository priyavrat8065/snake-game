from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)  # using keyword arguments
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)  # it is a kind of parda that hide what is happening behind the wall
# TODO: 1) Create a snake body
# when we create a turtle object. It is 20 x 20 pixels in dimension.
# Master branch contains Angela's code, my-work branch contains my code.
snake = Snake()

# TODO: 2) Move the snake
# We make the snake move forward in one direction without having to do anything

# to make something continuously happen, we achieve that by using while loop. so let's create game_is_on variable
game_is_on = True
while game_is_on:
    screen.update()  # it basically tells when to remove that parda.
    time.sleep(2)  # It is basically controlling the screen refresh rate. The sooner screen updates/Refresh, the
    # the faster snake appears to move.
    snake.move()


# TODO: 3) Create a snake class in a separate snake.py file


screen.exitonclick()
