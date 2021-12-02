from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)  # using keyword arguments
screen.bgcolor("black")
screen.title("My snake game")

# TODO: 1) Create a snake body
# when we create a turtle object. It is 20 x 20 pixels in dimension.
# Master branch contains Angela's code, my-work branch contains my code.
starting_positions = [(0, 0), (-20, 0), (-40, 0)]  # create a list of tuples where each tuple contains x and y
# coordinates.
segments = []
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

# TODO: 2) Move the snake
# We make the snake move forward in one direction without having to do anything
# to make something continuously happen, we achieve that by using while loop. so let's create game_is_on variable
game_is_on = True
while game_is_on:
    for seg in segments:
        seg.fd(20)
screen.exitonclick()
