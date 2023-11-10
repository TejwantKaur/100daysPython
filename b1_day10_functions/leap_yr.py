def leap_year(yr):
  if yr%4 == 0:
    if yr%100 == 0:
      return yr%400 == 0
    else:
      return True
  else:
    return False

def days_in_month(month, year):
  month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

  if leap_year(year) and month == 2:
    return 29
  return month_days[month-1]

year = int (input("Enter year: "))
month = int (input("Enter month: "))

days = days_in_month(month,year)
print(days)