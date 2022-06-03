#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random

seed = int(input("Creat a seed number "))
random.seed(seed)

heta = random.randint(1,2)

if heta == 1:
  print(""""
  ________________________
    `'-.,________,,..-  ___ \________
       > `'-.,_____,,.-`<_>\ )__     `\

         >            `'-._    _)____  \

          >          _.-'`  _______  `\ |
           >   _,,..--'''```       `'-.\|
          >-'``                        `' 
          """ ) 
else:
  print("""
       _///_
     /o    \/
     > ))_./\

        <
  """)