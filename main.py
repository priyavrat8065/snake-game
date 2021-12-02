from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)  # using keyword arguments
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)  # it is a kind of parda that hide what is happening behind the wall
# TODO: 1) Create a snake body
# when we create a turtle object. It is 20 x 20 pixels in dimension.
# Master branch contains Angela's code, my-work branch contains my code.
segments = []
gap = 0
for seg_pos in range(0, 3):
    new_part = Turtle("square")
    new_part.color("white")
    new_part.penup()
    new_part.goto(x=0 + gap, y=0)
    gap -= 20
    segments.append(new_part)

# TODO: 2) Move the snake
# We make the snake move forward in one direction without having to do anything

# to make something continuously happen, we achieve that by using while loop. so let's create game_is_on variable
game_is_on = True
while game_is_on:
    screen.update()  # it tells when to remove that parda.
    time.sleep(0.1)
    for pos in range(len(segments) - 1, 0, -1):
        new_x = segments[pos - 1].xcor()
        new_y = segments[pos - 1].ycor()
        segments[pos].goto(new_x, new_y)
    segments[0].fd(20)



screen.exitonclick()
