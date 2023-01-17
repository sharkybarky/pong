import time
from turtle import Screen

from ball import Ball
from field import Field
from paddle import Paddle
from scoreboard import Scoreboard

HEIGHT_PIXELS = 600
WIDTH_PIXELS = 600
MAX_X = WIDTH_PIXELS / 2
MAX_Y = HEIGHT_PIXELS / 2
MIN_X = - MAX_X
MIN_Y = - MAX_Y


def end_game():
    global run_game
    run_game = False


screen = Screen()
screen.setup(WIDTH_PIXELS, HEIGHT_PIXELS)
screen.bgcolor("black")

paddle_left = Paddle("l")
paddle_right = Paddle("r")

scoreboard_left = Scoreboard((-30, 270))
scoreboard_right = Scoreboard((30, 270))

# set tracer to 0 here only once field and paddles have all been drawn smoothly
screen.tracer(0)

field = Field(MIN_X, MIN_Y, MAX_X, MAX_Y)
ball = Ball(MIN_X, MIN_Y, MAX_X, MAX_Y)

screen.listen()
screen.onkeypress(fun=paddle_right.set_direction_up, key="Up")
screen.onkeypress(fun=paddle_right.set_direction_down, key="Down")
screen.onkeypress(fun=paddle_left.set_direction_up, key="w")
screen.onkeypress(fun=paddle_left.set_direction_down, key="s")
screen.onkeypress(fun=end_game, key="Escape")
run_game = True


def debug_info():
    print(f"{paddle_left.position()=}")
    print(f"{paddle_right.position()=}")
    print(f"{ball.distance(paddle_left.position())=}")
    print(f"{ball.distance(paddle_right.position())=}")
    print(f"{paddle_left.distance(paddle_right.position())=}")


while run_game:
    time.sleep(0.05)
    paddle_left.move()
    paddle_right.move()
    ball.move()
    screen.update()
    # compute any changes after movement happened

    # wall ricochet
    # if ball.wall_hit():
    #     ball.ricochet()
    debug_info()
    if ~ball.hit_last and (ball.distance(paddle_left) < 22 or ball.distance(paddle_right) < 18):
        ball.paddle_hit()
    elif not(ball.min_y < ball.ycor() < ball.max_y):
        ball.wall_ricochet()
    elif not(ball.min_x < ball.xcor() < ball.max_x):
        ball.out()

scoreboard_left.game_ended()
screen.update()
time.sleep(0.5)