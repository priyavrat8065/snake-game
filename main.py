from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)  # using keyword arguments
screen.bgcolor("black")
screen.title("My snake game")
# TODO: 1) Create a snake body
# when we create a turtle object. It is 20 x 20 pixels in dimension.
# Master branch contains Angela's code, my-work branch contains my code.
snake = []
gap = 0
for snake_part in range(0, 3):
    new_part = Turtle("square")
    new_part.color("white")
    new_part.goto(x=0 + gap, y=0)
    gap -= 20
    snake.append(new_part)
# TODO: 2) Move the snake
# We make the snake move forward in one direction without having to do anything

# to make something continuously happen, we achieve that by using while loop. so let's create game_is_on variable
game_is_on = True
while game_is_on:
    for snake_part in snake:
        snake_part.fd(20)




screen.exitonclick()