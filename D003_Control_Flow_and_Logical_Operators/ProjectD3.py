print("""
  .....................
 -    :     |     :    - 
'''''':''''' ''''':''''''
 `.    .    :    .    .'
   `.   .   :   .   .'
     `.  .  :  .  .'
       `. . : . .'
         `..:..'
           `:'
""")
print("Welcome to Jewel tower.")
print("Your mission is to find the Jewel.") 
print("You are at the entrance. Where do you want to go? ")
a = input("sewer or frontgate? ")
if a == 'frontgate':
  print("You need to go to the top of the tower. What will you do? ")
  b = input("use elevator or stairs? ")
  if b == 'elevator':
    print("You are now at the top of the tower and there are 3 doors.")
    c = print(input("Choose door blue, yellow, or red? "))
    if c == 'blue':
      print("Gameover, you flew from the sky")
    elif c == 'yellow':
      print("Congratulations!!!, you have found the Jewel")
    else:
      print("Gameover, you have entered the Dragon's nest")  
  else:
    print("Gameover, You encountered soldiers guarding the jewel")
else:
  print("Gameover, you encounterd monsters")