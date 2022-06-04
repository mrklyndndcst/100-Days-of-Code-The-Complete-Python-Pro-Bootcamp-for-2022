from turtle import Turtle


class Scoreboard(Turtle):
  
  def __init__(self):
    super().__init__()
    self.points = 0
    self.penup()
    self.color("white")
    self.speed(0)
    self.goto(0, 270)
    self.write(f"Score = {self.points}", align="center", font=("Verdana", 24, "normal"))
    self.hideturtle()
    
  def update_points(self):
    self.points += 1
    self.write(f"Score = {self.points}", align="center", font=("Verdana", 24, "normal"))
    
  def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER", align="center", font=("Verdana", 30, "normal"))
