from turtle import Turtle

FONT = ("Courier", 14, "normal")
ALIGNMENT = "center"


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

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 14, "normal"))
