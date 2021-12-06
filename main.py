from turtle import Screen
from snake_speed import time_delay
from food import Food
from snake import Snake
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()
# TODO: 3) Control the snake
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(time_delay)  # It is basically controlling the screen refresh rate. The sooner screen updates/Refresh,
    # the faster snake appears to move.
    # TODO: 2) Move the snake
    snake.move()
    if snake.head.distance(food) < 15:
        food.food_refresh()
        snake.extend()
        scoreboard.increment_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    for segment in snake.segments:
        if snake.head == segment:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
