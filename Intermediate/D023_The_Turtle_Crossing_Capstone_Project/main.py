import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Cross Road")
screen.listen()

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
  time.sleep(0.1)
  screen.update()
  
  car_manager.create_car()
  car_manager.move_cars()
  
  # game_over
  for car in car_manager.all_cars:
    if player.distance(car) < 20:
      game_is_on = False
      score.game_over()
      
  # player reach top
  if player.ycor() > 275:
    car_manager.level_up()
    player.level_up()
    score.clear()
    score.level_up()
    
screen.exitonclick()
