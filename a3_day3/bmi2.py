ht = float(input("Enter height in m: "))
wt = float(input("Enter weight in kg: "))

bmi = round(wt / ht **2) 

if bmi < 18.5 :
  print(f"Your bmi is {bmi}, You are Underweight")
elif bmi < 25 : 
  print(f"Your bmi is {bmi}, You are normal weight")
elif bmi < 30 :
  print(f"Your bmi is {bmi}, You are overWeight")
elif bmi < 35 :
  print(f"Your bmi is {bmi}, You are Obese")

else :
  print(f"Your bmi is {bmi}, You are clinically obese")
  