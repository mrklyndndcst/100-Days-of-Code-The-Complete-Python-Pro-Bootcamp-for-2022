from importlib.resources import path
import os


level = ''
foldername = ""
# enter day title here ↓↓↓
day = "Section 24: Day 24 - Intermediate - Files, Directories and Paths"

day_number = [int(word) for word in day.split() if word.isdigit()][0]

if "Beginner" in day:
  split_string = day.split("- Beginner - ", 1)
  project_title = split_string[1]
  level = "Beginner"
elif "Intermediate" in day:
  split_string = day.split("- Intermediate - ", 1)
  project_title = split_string[1]
  level = "Intermediate"
elif "Web Foundation" in day:
  split_string = day.split("- Web Foundation - ", 1)
  project_title = split_string[1]
  level = "Web_Foundation"
elif "Intermediate+" in day:
  split_string = day.split("- Intermediate+ ", 1)
  project_title = split_string[1]
  level = "Intermediate+"
elif "Advanced" in day:
  split_string = day.split("- Advanced - ", 1)
  project_title = split_string[1]
  level = "Advanced"
elif "Professional Portfolio Project" in day:
  split_string = day.split("- Professional Portfolio Project - ", 1)
  project_title = split_string[1]
  level = "Professional_Portfolio_Project"
else:
  print('edit day title')

foldername += f"D{day_number:03}_"

for i in project_title:
  if i == " ":
    foldername += "_"
  else:
    foldername += i

print(foldername)
  
path =  f"/Users/mdecosto/Desktop/study/udemy/100-Days-of-Code-The-Complete-Python-Pro-Bootcamp-for-2022/{level}/{foldername}"

os.mkdir(path)