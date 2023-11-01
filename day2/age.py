# 52 weeks

# if we to live 90 years, it will ask present age, and 
# then will tell how may months weeks and days are left

currAge = int(input("Write your current age: "))

totalYears = 90
yrLeft = 90 - currAge

daysLeft = yrLeft * 365
weeksLeft = yrLeft * 52
monthLeft = yrLeft * 12

print(f"You have {daysLeft} days, {weeksLeft} weeks, {monthLeft} month")
# print(weeksLeft)
# print(monthLeft)

