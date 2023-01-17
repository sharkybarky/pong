import random
from turtle import Turtle

RIGHT = 0
LEFT = 180
DOWN = 270
UP = 90


class Ball(Turtle):
    move_states = {"serve_l": 0, "serve_r": 0, "l_to_r": -1, "r_to_l": 1, "out": 0}

    def __init__(self, min_x, min_y, max_x, max_y):
        super().__init__()
        # left paddle starts with ball
        self.move_state = random.choice(["serve_l", "serve_r"])
        self.shape("circle")
        self.turtlesize(2)
        self.min_x = min_x + 5
        self.min_y = min_y + 5
        self.max_x = max_x - 5
        self.max_y = max_y - 5
        self.color("blue")
        self.fillcolor("blue")
        self.penup()
        self.hit_last = False
        self.goto_serve()

    def goto_serve(self):
        rand_angle = random.randint(-70, 70)
        if self.move_state == "serve_l":
            self.goto((self.min_x + 37), 17)
            self.setheading(360 + rand_angle)
        elif self.move_state == "serve_r":
            self.goto((self.max_x - 37), 17)
            self.setheading(180 + rand_angle)

    def move(self):
        if self.move_state == "out":
            pass
        elif self.move_state in ["l_to_r", "r_to_l"]:
            pass
        elif self.move_state == "serve_l":
            self.move_state = "r_to_l"
        elif self.move_state == "serve_r":
            self.move_state = "l_to_r"

        self.forward(5 * self.move_states[self.move_state])
        self.hit_last = False

    def paddle_hit(self):
        if self.move_state == "r_to_l":
            self.move_state = "l_to_r"
        elif self.move_state == "l_to_r":
            self.move_state = "r_to_l"
        else:
            return

        self.hit_last = True

    def wall_ricochet(self):
        heading = self.heading()
        self.setheading((-1 * heading) + 360)

    def out(self):
        self.move_state = "out"

