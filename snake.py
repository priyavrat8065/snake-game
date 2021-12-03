from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # change the name of first turtle object(segments[0]) in the list segments to head

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_pos in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_pos - 1].xcor()
            new_y = self.segments[seg_pos - 1].ycor()
            self.segments[seg_pos].goto(new_x, new_y)
        self.head.fd(20)

    def move_down(self):
        current_direction = self.head.heading()
        if current_direction != UP:
            self.head.setheading(270)

    def move_left(self):
        current_direction = self.head.heading()
        if current_direction != RIGHT:
            self.head.setheading(180)

    def move_right(self):
        current_direction = self.head.heading()
        if current_direction != LEFT:
            self.head.setheading(0)

    def move_up(self):
        current_direction = self.head.heading()
        if current_direction != DOWN:
            self.head.setheading(90)
