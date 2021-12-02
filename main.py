from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)  # using keyword arguments
screen.bgcolor("black")
screen.title("My snake game")

# TODO: 1) Create a snake body
# when we create a turtle object. It is 20 x 20 pixels in dimension.
# Master branch contains Angela's code, my-work branch contains my code.
segment_1 = Turtle("square")
segment_1.color("white")
segment_1.goto(0, 0)

segment_2 = Turtle("square")
segment_2.color("white")
segment_2.goto(-20, 0)

segment_3 = Turtle("square")
segment_3.color("white")
segment_3.goto(-40, 0)


screen.exitonclick()