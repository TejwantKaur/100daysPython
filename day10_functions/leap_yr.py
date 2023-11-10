yr = int (input("Enter a year you wanna check "))

def leap_year():
  if yr%4 == 0:
    if yr%100 == 0:
      return yr%400 == 0
    else:
      return True
  else:
    return False