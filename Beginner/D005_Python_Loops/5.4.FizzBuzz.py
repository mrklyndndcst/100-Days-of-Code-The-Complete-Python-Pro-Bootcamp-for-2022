# Write your code below this row 👇
for list in range(1, 101):
  if (list % 15) == 0:
    print("FizzBuzz")
  elif (list % 5) == 0 :
    print("Buzz")
  elif (list % 3) == 0:
    print("Fizz")
  else:
    print(list)