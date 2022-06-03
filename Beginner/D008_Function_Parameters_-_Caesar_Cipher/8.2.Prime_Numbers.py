#Write your code below this line 👇

def prime_checker(number):
  equal = 0
  while  equal != 1:
    for check in range(1, number):
      if number%check == 0:
        equal += 1
    if equal == 1:
      print("It's a prime number.")
    else:
      print("It's not a prime number.")
      break
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number = n)