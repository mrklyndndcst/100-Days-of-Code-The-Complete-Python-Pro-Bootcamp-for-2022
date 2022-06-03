import random
rock = "👊"
paper = "✋"
scissors = "✌️"
choices = [rock, paper, scissors]
player = int(input(f"What do you choose? type 1 for {rock}, 2 for {paper} or 3 for {scissors}\n"))
print("You choose")
if player < 1 or player > 3:
  print("Invalid")
  ai = random.randint(1 , 3)
  print("Artificial Intelligence choose")
  print(choices[ai - 1])
  print("You loose!, please follow simple instructions..")
elif player >= 1 or player <= 3:
  print(choices[player - 1])

  ai = random.randint(1 , 3)
  print("Artificial Intelligence choose")
  print(choices[ai - 1])
  if player == ai:
    print("Draw!, Try again..")
  elif player == 1 and ai == 2 or player == 2 and ai == 3 or player == 3 and ai == 1:
    print("You loose!, Pay your debt..")
  else:
    print("You Win!, get your rewards..")

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# if user_choice >= 3 or user_choice < 0: 
#   print("You typed an invalid number, you lose! ") 
# else:
#   print(game_images[user_choice])

#   computer_choice = random.randint(0, 2)
#   print("Computer chose:")
#   print(game_images[computer_choice])

#   if user_choice == 0 and computer_choice == 2:
#     print("You win!")
#   elif computer_choice == 0 and user_choice == 2:
#     print("You lose")
#   elif computer_choice > user_choice:
#     print("You lose")
#   elif user_choice > computer_choice:
#     print("You win!")
#   elif computer_choice == user_choice:
#     print("It's a draw")