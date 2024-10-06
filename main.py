from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

l_paddle = Paddle((-360, 0))
r_paddle = Paddle((360, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=l_paddle.move_up)
screen.onkey(key="Down", fun=l_paddle.move_down)
screen.onkey(key="w", fun=r_paddle.move_up)
screen.onkey(key="s", fun=r_paddle.move_down)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision of the ball with the wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision of the ball with the paddle.
    if l_paddle.distance(ball) < 50 and ball.xcor() < -340 or r_paddle.distance(ball) < 50 and ball.xcor() > 340:
        # 50 because that covers the entire paddle, and 340 because it's the perfect distance to only
        # collide with the paddle, because the screen only goes to 400, also minding the size of the
        # ball and the paddle. ((pos of paddle 360 - 10 of half the paddle) - (340 + 10 of half the ball)) = 0.
        # That's the justification.
        ball.hit()

    # Detect score.
    if ball.xcor() > 380:
        scoreboard.increase_l_score()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.increase_r_score()
        ball.reset_position()





screen.exitonclick()