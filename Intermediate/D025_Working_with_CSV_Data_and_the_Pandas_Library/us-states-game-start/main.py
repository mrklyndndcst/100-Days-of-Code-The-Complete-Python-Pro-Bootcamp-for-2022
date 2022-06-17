import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "Intermediate/D025_Working_with_CSV_Data_and_the_Pandas_Library/us-states-game-start/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# # get the coordinate of states
# def get_mouse_click_coor(x, y):
#   print(x,y)
  
# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()


data = pd.read_csv("Intermediate/D025_Working_with_CSV_Data_and_the_Pandas_Library/us-states-game-start/50_states.csv")


correct = []
correct_guesses = 0
run = True
while run == True:
  answer_state = screen.textinput(title=f"{correct_guesses}/50 States Correct", prompt="What's another state's name?")
  if answer_state == "exit":
    run = False
  for i in data.state:
    if i.lower() == answer_state.lower():
      x = int(data[data.state == i].x)
      y = int(data[data.state == i].y)
      correct_answer = turtle.Turtle()
      correct_answer.penup()
      correct_answer.hideturtle()
      correct_answer.goto(x, y)
      correct_answer.write(i, align="center", font=10)
      correct.append(correct_answer)
      correct_guesses += 1

turtle.exitonclick()
