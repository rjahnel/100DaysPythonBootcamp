def is_leap(year):
  result = False
  
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        result = True
      else:
        result = False
    else:
      result = True
  else:
    result = False
  return result

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  days = month_days[month-1]
  if days == 28:
    if is_leap(year):
      days = 29
  return days
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












