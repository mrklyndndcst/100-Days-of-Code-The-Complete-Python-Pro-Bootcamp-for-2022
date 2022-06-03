#Password Generator Project
import random
let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sym = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nlet = int(input("How many letters would you like in your password?\n")) 
nnum = int(input(f"How many numbers would you like?\n"))
nsym = int(input(f"How many symbols would you like?\n"))

plet = ""
for letter in range(0 , nlet):
  x = random.randint(0, len(let)-1)
  plet += let[x]

pnum = ""
for number in range(0 , nnum):
  y = random.randint(0, len(num)-1)
  pnum += num[y]

psym = ""
for symbol in range(0 , nsym):
  z = random.randint(0, len(sym)-1)
  psym += sym[z]

epwd = list(plet+pnum+psym)
random.shuffle(epwd) #random code stored in epwd
hpwd = ""
for hard in epwd:
  hpwd += hard
print(f"Here is your 1st password:\n{hpwd}")

epassword = "" #######100 days of python sample################
for character in range(0 , nlet):
  epassword += random.choice(let)

for character in range(0 , nnum):
  epassword += random.choice(num)

for character in range(0,nsym):
  epassword += random.choice(sym)

lpwd = list(epassword)
random.shuffle(lpwd)
password = ""
for character in lpwd:
  password += character
print(f"Here is your 2nd password:\n{password}")
print("Choose any")