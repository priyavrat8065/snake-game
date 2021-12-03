from turtle import Screen

from scoreboard import Scoreboard
from food import Food
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
food = Food()
scoreboard = Scoreboard()
# TODO: 3) Control the snake
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
# TODO: 2) Move the snake
# We make the snake move forward in one direction without having to do anything

# to make something continuously happen, we achieve that by using while loop. so let's create game_is_on variable
game_is_on = True
while game_is_on:
    screen.update()  # it basically tells when to remove that parda.
    time.sleep(0.1)  # It is basically controlling the screen refresh rate. The sooner screen updates/Refresh, the
    # the faster snake appears to move.
    snake.move()
    if snake.segments[0].distance(food) < 15:
        food.food_refresh()
        scoreboard.increment_score()


# TODO: 3) Create a snake class in a separate snake.py file


screen.exitonclick()
