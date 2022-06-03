def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return "Leap year."
      else:
        return "Not leap year."
    else:
      return "Leap year."
  else:
    return "Not leap year."

def days_in_month(year , month):
  if month > 12 or month < 1:
    checking = True
    while checking is True:
      month = int(input("We only have 12 months in a year. Please choose from 1 to 12: "))
      if month >= 1 or month <= 12:
        checking = False
    checking = True
  leap = is_leap(year)
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if leap == "Leap year.":
    month_days[1] = 29
  return month_days[month - 1]
    
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)