from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

game_is_on = True
while game_is_on:
  time.sleep(ball.ball_speed)
  screen.update()
  ball.move()
  
  if ball.ycor() > 290 or ball.ycor() < -270:
    ball.bounce_y()

  #collision with the paddle
  if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()
    
  # score
  if ball.xcor() > 380 or ball.xcor() < -380 :
    score.clear()
    if ball.xcor() > 380:
      score.add_l_score()
    else:
      score.add_r_score()
    ball.reset_position()

    
  
screen.exitonclick()