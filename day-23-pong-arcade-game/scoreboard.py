from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 70, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.color("white")
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)

    def r_increase(self):
        self.r_score += 1
        self.update_scoreboard()

    def l_increase(self):
        self.l_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
