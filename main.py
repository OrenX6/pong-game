# TODO: Create the screen
# TODO: Create and move paddle
# TODO: Create another paddle
# TODO: Create a ball and make it move
# TODO: Detect collision with wall and bounce
# TODO: Detect collision with paddle
# TODO: Detect when paddle missed and score
# TODO: keep score


"""
Notes:
The default size of a Turtle object is 20 pixels,
which is the equivalent of the ratio 1 when resizing the Turtle .

"""""

import time
from turtle import Screen  # function

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()  # returns a singleton object of a TurtleScreen subclass
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # turns automatic screen updates off and set delay for update()

ball = Ball()
scoreboard = Scoreboard()

paddle_a = Paddle((350, 0))
paddle_b = Paddle((-350, 0))

screen.listen()  # focus on TurtleScreen in order to collect key-events

screen.onkeypress(paddle_a.move_up, "Up")
screen.onkeypress(paddle_a.move_down, "Down")
screen.onkeypress(paddle_b.move_up, "w")
screen.onkeypress(paddle_b.move_down, "s")

game_is_on = True

while game_is_on:

    ball.move()

    if abs(ball.ycor()) >= 290:  # ball collisions with walls
        ball.bounce_y()
    elif ball.xcor() >= 330 and ball.distance(paddle_a) < 53:  # ball collisions with paddle a:
        ball.setx(330)
        ball.bounce_x()
        ball.increase_speed()
    elif ball.xcor() <= -330 and ball.distance(paddle_b) < 53:  # ball collisions with paddle b:
        ball.setx(-330)
        ball.bounce_x()
        ball.increase_speed()
    elif ball.xcor() >= 400:  # if the ball goes out of right bound
        scoreboard.l_point()
        ball.reset_position()
    elif ball.xcor() <= -400:  # if the ball goes out of left bound
        scoreboard.r_point()
        ball.reset_position()

    # latest version of the drawing
    screen.update()  # Perform a TurtleScreen update. To be used when tracer is turned off.

    time.sleep(1/60)  # 16.667 milliseconds

screen.exitonclick()




