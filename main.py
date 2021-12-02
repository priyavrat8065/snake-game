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
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)

screen.exitonclick()
