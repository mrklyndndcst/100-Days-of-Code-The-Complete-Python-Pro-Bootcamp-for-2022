# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
yday = 365
yweek = 52
ymonth = 12
mday = 90 * 365
mweek = 90 * 52
mmonth = 90 * 12
ageint = int(age)

print(f"You have {mday - (ageint * yday)} days, {mweek - (ageint * yweek)} weeks, and {mmonth - (ageint * ymonth)} months left.")