yr = int (input("Enter a year you wanna check "))

# 2100 % 4 == 0 but not a leap year,1900
if yr % 4 == 0:
  if yr % 100 == 0:
    if yr % 400 == 0:
      print("Leap Year")
    else :
      print("Not a leap year")
  else :
    print("Leap year")
else :
  print("Not a leap year")