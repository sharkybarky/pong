from turtle import Turtle

FONT = ("Arial", 20, "bold")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score_position = position
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.score = -1
        self.update()

    def update(self):
        self.score += 1
        self.clear()
        self.goto(self.score_position)
        self.write(arg=f"{self.score}",
                   align=ALIGNMENT,
                   font=FONT)

    def game_ended(self):
        self.goto(0, 0)
        self.pencolor("red")
        self.write(arg=f"Game Over!", align=ALIGNMENT, font=FONT)
