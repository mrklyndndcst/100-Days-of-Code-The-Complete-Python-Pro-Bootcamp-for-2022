from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# tim = Turtle()
# tim.speed(0)
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score = Scoreboard()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()

  #Detect collision with food.
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    score.clear()
    score.update_points()

  #Detect collision with food.
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    game_is_on = False
    score.game_over()
    
  #Detect collision with food.
  for segment in snake.segments[2:]:
    if snake.head.distance(segment) < 10:
      game_is_on = False
      score.game_over()


screen.exitonclick()