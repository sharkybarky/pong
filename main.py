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

paddle_left = Paddle(-280, 0)
paddle_right = Paddle(265, 0)

scoreboard_left = Scoreboard((-30, 265))
scoreboard_right = Scoreboard((30, 265))

# set tracer to 0 here only once field and paddles have all been drawn smoothly
screen.tracer(0)

field = Field(MIN_X, MIN_Y, MAX_X, MAX_Y)
ball = Ball(MIN_X, MIN_Y, MAX_X, MAX_Y)

screen.listen()
screen.onkeypress(fun=paddle_right.move_up, key="Up")
screen.onkeypress(fun=paddle_right.move_down, key="Down")
screen.onkeypress(fun=paddle_left.move_up, key="w")
screen.onkeypress(fun=paddle_left.move_down, key="s")
screen.onkeypress(fun=end_game, key="Escape")
run_game = True


def debug_info():
    print(f"{ball.in_play()=}")
    print(f"{paddle_left.position()=}")
    print(f"{paddle_right.position()=}")
    print(f"{ball.position()=}")
    print(f"{ball.heading()=}")
    print(f"{ball.distance(paddle_left.position())=}")
    print(f"{ball.distance(paddle_right.position())=}")


while run_game:
    time.sleep(0.03)
    ball.move()
    screen.update()

    # compute if any events occurred after movement happened
    debug_info()
    # tweak the paddle y positions to the middle of the paddle as the turtle position is the bottom left corner
    # if ball.in_play() and (ball.distance(paddle_left) < 21 or ball.distance(paddle_right) < 18):
    if ball.in_play() and \
            (paddle_left.hit(ball.xcor() - 20, ball.ycor()) or paddle_right.hit(ball.xcor() + 20, ball.ycor())):
        ball.paddle_hit()
        print("HIT!!!!!!!")
    elif not(ball.min_y < ball.ycor() < ball.max_y):
        ball.wall_ricochet()
    elif not(ball.min_x < ball.xcor() < ball.max_x):
        ball.out()
        if ball.min_x > ball.xcor():
            scoreboard_right.update()
        else:
            scoreboard_left.update()
        ball.goto_serve()


scoreboard_left.game_ended()
screen.update()
time.sleep(0.5)
