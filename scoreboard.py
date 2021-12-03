from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.update_scoreboard()

    def increment_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 14, "normal"))
