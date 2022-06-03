from replit import clear
import Calculator_Art

def add(n1, n2): #add
 return n1 + n2

def sub(n1, n2): #subtract
  return n1 - n2

def mul(n1, n2): #multiply
  return n1 * n2

def div(n1, n2): #divide
  return n1 / n2 

operations = { 
  "+" : add, 
  "-" : sub, 
  "*" : mul, 
  "/" : div
  } #dictionary of functions

def calculator():
  print(Calculator_Art.logo)
  num1 = int(input("What's the first number?: "))  
  run = True
  while run == True:
    for symbol in operations:
      print(symbol)
    math = input("Pick an operation: ")
    num2  = int(input("What's the next number?: "))  
    answer = operations[math](n1 = num1 , n2 = num2)
    clear()
    print(f"The answer is: \n{answer} ")
    again = True
    while again == True:
      proceed = input("do you want to continue calculating with answer? 'y' for yes or 'n' for no: ")
      if proceed == "y": 
        again = False
        run = True
        num1 = answer
      elif proceed == "n":
        again = False
        run = False
      else:
        print("Type 'y' for yes and 'n' for no only: ")
    
overall_run = True
while overall_run == True:
  calculator()
  again = True
  while again == True:  
    test = input("Run again? 'y' for yes or 'n' for no: ")
    if test == 'n':
      again = False 
      overall_run = False
    elif test == 'y':
      overall_run = True
      again = False
    else:
      print("Invalid input")

#  yy   yy  uu  uu 
#   yy yy   uu  uu
#    yy     uu  uu
#    yy     uu  uu 
#    yy      uuuu     version below 

# from replit import clear
# from art import logo

# def add(n1, n2):
#   return n1 + n2

# def subtract(n1, n2):
#   return n1 - n2

# def multiply(n1, n2):
#   return n1 * n2

# def divide(n1, n2):
#   return n1 / n2

# operations = {
#   "+": add,
#   "-": subtract,
#   "*": multiply,
#   "/": divide
# }

# def calculator():
#   print(logo)

#   num1 = float(input("What's the first number?: "))
#   for symbol in operations:
#     print(symbol)
#   should_continue = True
 
#   while should_continue:
#     operation_symbol = input("Pick an operation: ")
#     num2 = float(input("What's the next number?: "))
#     calculation_function = operations[operation_symbol]
#     answer = calculation_function(num1, num2)
#     print(f"{num1} {operation_symbol} {num2} = {answer}")

#     if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
#       num1 = answer
#     else:
#       should_continue = False
#       clear()
#       calculator()

# calculator()