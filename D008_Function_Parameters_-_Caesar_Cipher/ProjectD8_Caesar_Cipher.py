import Caesar_Cipher_Art
from replit import clear

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cyphere(message, shift_value):
  output = ""
  if direction == "decode":
    shift_value *= -1  
  for letter in message:
    if letter in alphabet:
      shifted = (alphabet.index(letter) + shift_value) % 26
      output += alphabet[shifted]
    else:
      output += letter   
  if direction == "encode" or direction == "decode":
    print(f"The {direction}d text is \n{output}")
  else:
    print("Your request is not included in our services. Please try again.")
run = "Y"
while run == "Y":
  clear()
  print(Caesar_Cipher_Art.logo)
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  cyphere(message = text, shift_value = shift)
  run = input("do you want to run again? type Y for Yes and N for No:\n")
  if run == "N":
    print("Thank you for choosing our service, Take care and Godbless")
  elif run != "Y" or run != "N":
    print("You are undecided, hope your satisfied with our service, Thank You and Godbless.")
    run == "N"

#  yy   yy  uu  uu 
#   yy yy   uu  uu
#    yy     uu  uu
#    yy     uu  uu 
#    yy      uuuu     version below 

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#     shift_amount *= -1
#   for char in start_text:
#     if char in alphabet:
#       position = alphabet.index(char)
#       new_position = position + shift_amount
#       end_text += alphabet[new_position]
#     else:
#       end_text += char

#   print(f"Here's the {cipher_direction}d result: {end_text}")

# from art import logo
# print(logo)

# should_continue = True
# while should_continue:
#   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#   text = input("Type your message:\n").lower()
#   shift = int(input("Type the shift number:\n"))

#   shift = shift % 26
#   caesar(start_text=text, shift_amount=shift, cipher_direction=direction)