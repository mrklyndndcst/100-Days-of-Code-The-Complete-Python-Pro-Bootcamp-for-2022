from replit import clear
import random
import Hangman_art
import Hangman_word

talo = Hangman_art.talo
word_list = Hangman_word.word_list
chosen_word = random.choice(word_list)

print(Hangman_art.logo)
display = []

for letters in chosen_word:
  display += "_"
print(f"The Chosen word is \n {display}")  
check = list(chosen_word)
life = 5
while check != display and life != 0:
  
  guess = input("Choose any letter. ")
  guess = guess.lower()

  clear()

  for n in range(len(chosen_word)):
    if chosen_word[n] == guess:
      display.pop(n)
      display.insert(n , guess) 
  for a in range(0,1):
    if guess not in chosen_word:
      life -= 1
      print(talo[life])
      print(f"The letter {guess} is not in the word, you loose a life")
    else:
      print(f"The letter {guess} is in the word")  
  print(display)
  if display == check:
    print("You win...") 
  elif life == 0:
    print("You loose...") 

#  yy   yy  uu  uu 
#   yy yy   uu  uu
#    yy     uu  uu
#    yy     uu  uu 
#    yy      uuuu     version below 

# from replit import clear
# import random

# from hangman_words import word_list
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# end_of_game = False
# lives = 6

# from hangman_art import logo, stages
# print(logo)

# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"

# while not end_of_game:
#     guess = input("Guess a letter: ").lower()

#     clear()

#     if guess in display:
#       print(f"You've already guessed {guess}")

#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter

#     #Check if user is wrong.
#     if guess not in chosen_word:

#         print(f"You guessed {guess}, that's not in the word. You lose a life.")
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")

#     #Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")

#     #Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")

#     print(stages[lives])