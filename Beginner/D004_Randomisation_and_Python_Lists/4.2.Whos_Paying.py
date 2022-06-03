import random
seed = random.seed(input("Enter a unique code here. "))
#Write your code above this line 👆
# 🚨 Don't change the code below 👇
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
max = len(names)
# print(max)
rand = random.randint(0, max-1)
# print(rand)
name = names[rand]
print(f"{name} is going to buy the meal today!")