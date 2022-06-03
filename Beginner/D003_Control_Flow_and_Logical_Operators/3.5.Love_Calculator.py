# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
T = (name1.lower()).count('t') + (name2.lower()).count('t')
R = (name1.lower()).count('r') + (name2.lower()).count('r')
U = (name1.lower()).count('u') + (name2.lower()).count('u')
E = (name1.lower()).count('e') + (name2.lower()).count('e')
L = (name1.lower()).count('l') + (name2.lower()).count('l')
O = (name1.lower()).count('o') + (name2.lower()).count('o')
V = (name1.lower()).count('v') + (name2.lower()).count('v')
true = T + R + U + E
love = L + O + V + E
tl = str(true)+str(love)
truelove = int(tl)

if truelove < 10 or truelove > 90:
  print(f"Your score is {truelove}, you go together like coke and mentos.")
elif truelove >= 40 and truelove <= 50:
  print(f"Your score is {truelove}, you are alright together.")
else:
  print(f"Your score is {truelove}")