from turtle import Turtle

RIGHT = 0
LEFT = 180
DOWN = 270
UP = 90


class Paddle(Turtle):
    def __init__(self, start_x_cord, start_y_cord):
        super().__init__()
        self.direction_multiplier = 0
        self.shape("square")
        self.shapesize(5, 1)
        self.pencolor("white")
        self.fillcolor("white")
        # starting position
        self.penup()
        self.goto(start_x_cord, start_y_cord)
        # self.debug_turtle = Turtle()
        # self.debug_turtle.shape("classic")
        # self.debug_turtle.pencolor("red")
        # self.debug_turtle.penup()

    def move_up(self):
        new_x_pos = self.xcor()
        new_y_pos = self.ycor() + 20
        self.goto(new_x_pos, new_y_pos)
        # self.debug()

    def move_down(self):
        new_x_pos = self.xcor()
        new_y_pos = self.ycor() - 20
        self.goto(new_x_pos, new_y_pos)
        # self.debug()

    def set_direction_up(self):
        self.direction_multiplier = 1

    def set_direction_down(self):
        self.direction_multiplier = -1

    def move_continuously(self):
        if self.direction_multiplier is not 0:
            self.forward(10 * self.direction_multiplier)

        # stop when out of bounds
        if not(-282 < self.ycor() < 260):
            self.direction_multiplier = 0

    def hit(self, x_coord, y_coord):
        # determine if left or right paddle, as face position differs by width of bat and whether
        # bat is in left or right position
        if self.xcor() > 0:
            x_adj = -10
        else:
            x_adj = 10

        paddle_face = {"x_line": self.xcor() + x_adj,
                       "y_top": self.ycor() + 50,
                       "y_bottom": self.ycor() - 50}
        # return true if any of the incoming co-ords are deemed to have gone past the paddles face
        if (abs(paddle_face["x_line"]) < abs(x_coord)) and \
                (paddle_face["y_bottom"] < y_coord < paddle_face["y_top"]):
            self.fillcolor("white")
            return True
        else:
            return False

    def debug(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.debug_turtle.goto(x_cor - 10, y_cor)
        print(f"{self.debug_turtle.pos()=}")
        self.debug_turtle.pendown()
        self.debug_turtle.left(90)
        self.debug_turtle.forward(50)
        self.debug_turtle.right(90)
        self.debug_turtle.forward(20)
        self.debug_turtle.right(90)
        self.debug_turtle.forward(100)
        self.debug_turtle.right(90)
        self.debug_turtle.forward(20)
        self.debug_turtle.right(90)
        self.debug_turtle.forward(50)
        self.debug_turtle.right(90)
        print(f"{self.debug_turtle.pos()=}")

