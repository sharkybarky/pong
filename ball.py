import random
from turtle import Turtle

RIGHT = 0
LEFT = 180
DOWN = 270
UP = 90


class Ball(Turtle):
    move_states = {"serve_from_l": 0, "serve_from_r": 0, "in_play": -1, "out": 0}

    def __init__(self, min_x, min_y, max_x, max_y):
        super().__init__()
        # left paddle starts with ball
        self.min_x = min_x + 5
        self.min_y = min_y + 5
        self.max_x = max_x - 5
        self.max_y = max_y - 5
        self.min_in_play_x = self.min_x
        self.max_in_play_x = self.max_x
        self.shape("circle")
        self.turtlesize(2)
        self.color("blue")
        self.fillcolor("blue")
        self.penup()
        self.x_move = 0
        self.y_move = 0
        self.move_state = "out"
        self.goto_serve()

    def goto_serve(self):
        self.clear()
        self.move_state = random.choice(["serve_from_r", "serve_from_l"])
        if self.move_state == "serve_from_l":
            self.goto(self.min_in_play_x + 40, 17)
            self.x_move = 3
            self.y_move = 3
        elif self.move_state == "serve_from_r":
            self.goto(self.max_in_play_x - 70, 17)
            self.x_move = -3
            self.y_move = -3

    def move(self):
        new_x_pos = self.xcor() + self.x_move
        new_y_pos = self.ycor() + self.y_move
        self.goto(new_x_pos, new_y_pos)
        self.move_state = "in_play"

    def paddle_hit(self):
        # ~1 as this ensures hits speed up the game gradually
        self.x_move *= -1.4
        # hits reduce y component to make ball move more directly
        self.y_move *= 0.7

    def wall_ricochet(self):
        # wall hit reduces x velocity
        self.x_move *= 0.8
        # assume perfect elasticity of bounce
        self.y_move *= -1

    def out(self):
        self.move_state = "out"
        self.x_move = 0
        self.y_move = 0

    def in_play(self):
        return self.min_in_play_x < self.xcor() < self.max_in_play_x

