import random
import Guess_The_Number_Art
from replit import clear

clear()
print(Guess_The_Number_Art.logo)
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

number = random.randint(1,100)
total_guess = 0

if level == "easy":
    total_guess += 10
elif level == "hard":
    total_guess += 5
    
while total_guess != 0:
    if total_guess > 1:
        print(f"You have {total_guess} attempts remaining to guess the number.")
    else:
        print(f"You have {total_guess} attempt remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess < number:
        print("Too low.")        
        print("Guess again.")
        total_guess -= 1
    elif guess > number:
        print("Too high.")
        print("Guess again.")
        total_guess -= 1
    else:
        print(f"You got it! The answer was {number}.")
        total_guess = 0
    if total_guess == 0 and guess != number:
        print("You've run out of guesses, you lose.")