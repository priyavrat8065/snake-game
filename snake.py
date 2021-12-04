from turtle import Turtle

SNAKE_LENGTH = 3
START_POS_X = 0
START_POS_Y = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.gap = 0
        self.create_snake()

    def create_snake(self):
        for seg_pos in range(SNAKE_LENGTH):
            new_part = Turtle("square")
            new_part.color("white")
            new_part.penup()
            new_part.goto(x=START_POS_X - self.gap, y=START_POS_Y)
            self.gap += 20
            self.segments.append(new_part)

    def increment_snake_len(self):
        new_part = Turtle("square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(self.segments[-1].position())
        self.segments.append(new_part)

    def move(self):
        for seg_pos in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_pos - 1].xcor()
            new_y = self.segments[seg_pos - 1].ycor()
            self.segments[seg_pos].goto(new_x, new_y)
        self.segments[0].fd(20)

    def move_down(self):
        current_direction = self.segments[0].heading()
        if current_direction != 90:
            self.segments[0].setheading(270)

    def move_left(self):
        current_direction = self.segments[0].heading()
        if current_direction != 0:
            self.segments[0].setheading(180)

    def move_right(self):
        current_direction = self.segments[0].heading()
        if current_direction != 180:
            self.segments[0].setheading(0)

    def move_up(self):
        current_direction = self.segments[0].heading()
        if current_direction != 270:
            self.segments[0].setheading(90)
