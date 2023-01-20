from turtle import Turtle


class Field(Turtle):
    def __init__(self, min_x, min_y, max_x, max_y):
        super().__init__()
        self.penup()
        self.speed(0)
        # draw centre line
        self.goto((min_x + max_x) / 2, max_y)
        self.pendown()
        self.pencolor("white")
        self.goto((min_x + max_x) / 2, min_y)


