from turtle import Turtle

class Scoreboard(Turtle):
  
  def __init__(self):
    super().__init__()
    with open("Intermediate/D021_Build_the_Snake_Game_Part_2:_Inheritance_&_List_Slicing/data.txt") as file:
      contents = file.read()
    self.points = 0
    self.high_score = int(contents)
    self.penup()
    self.color("white")
    self.speed(0)
    self.goto(0, 270)
    self.update_scoreboard()
    self.hideturtle()
    
  def update_points(self):
    self.points += 1
    self.update_scoreboard()
    
  def update_scoreboard(self):
    self.write(f"Score = {self.points} Highest Score = {self.high_score}", align="center", font=("Verdana", 24, "normal"))
    
  def reset(self):
    if self.points > self.high_score:
      self.high_score = self.points
      with open("Intermediate/D021_Build_the_Snake_Game_Part_2:_Inheritance_&_List_Slicing/data.txt", mode="w") as file:
        file.write(str(self.points))
    self.points = 0
    self.clear()
    self.update_scoreboard()