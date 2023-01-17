from turtle import Turtle

RIGHT = 0
LEFT = 180
DOWN = 270
UP = 90


class Paddle(Turtle):
    def __init__(self, left_or_right):
        super().__init__()
        self.direction = 0
        self.screen.register_shape("paddle", ((0, 0), (0, 40), (5, 40), (5, 0)))
        # starting position
        self.shape("paddle")
        self.penup()
        match left_or_right:
            case "l":
                self.goto(-280, 0)
            case "r":
                self.goto(270, 0)
        self.pencolor("white")
        self.fillcolor("white")
        self.setheading(90)

    def set_direction_up(self):
        self.direction = 1

    def set_direction_down(self):
        self.direction = -1

    def move(self):
        if self.direction is not 0:
            self.forward(10 * self.direction)

        if not(-282 < self.ycor() < 260):
            self.direction = 0
