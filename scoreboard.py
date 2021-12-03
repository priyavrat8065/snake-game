from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.initial_score()

    def increment_score(self):
        self.clear()
        self.goto(x=0, y=280)
        self.write(arg="Score:", move=False, align="right", font=("Arial", 14, "bold"))
        self.score += 1
        self.goto(x=10, y=280)
        self.write(self.score, align="right", font=("Arial", 14, "bold"))

    def initial_score(self):
        self.goto(x=0, y=280)
        self.write(arg="Score:", move=False, align="right", font=("Arial", 14, "bold"))
        self.goto(x=10, y=280)
        self.write(self.score, align="right", font=("Arial", 14, "bold"))


