from importlib.resources import path
import os


level = ''
foldername = ""
# enter day title here ↓↓↓
day = "Section 20: Day 20 - Intermediate - Build the Snake Game Part 1: Animation & Coordinates"

day_number = [int(word) for word in day.split() if word.isdigit()][0]

if "Beginner" in day:
  split_string = day.split("- Beginner - ", 1)
  project_title = split_string[1]
  level = "Beginner"
elif "Intermediate" in day:
  split_string = day.split("- Intermediate - ", 1)
  project_title = split_string[1]
  level = "Intermediate"
else:
  print('edit program')

foldername += f"D{day_number:03}_"

for i in project_title:
  if i == " ":
    foldername += "_"
  else:
    foldername += i

print(foldername)
  
path =  f"/Users/mdecosto/Desktop/study/udemy/100-Days-of-Code-The-Complete-Python-Pro-Bootcamp-for-2022/{level}/{foldername}"

os.mkdir(path)