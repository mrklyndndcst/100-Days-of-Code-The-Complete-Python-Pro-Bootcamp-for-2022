from importlib.resources import path
import os

# enter day title here ↓↓↓
day = "D019 Intermediate - Instances, State and Higher Order Functions"
foldername = ""

for i in day:
  if i == " ":
    foldername += "_"
  else:
    foldername += i
    
path =  f"/Users/mdecosto/Desktop/study/udemy/100-Days-of-Code-The-Complete-Python-Pro-Bootcamp-for-2022/{foldername}"

os.mkdir(path)