print("Welcome to Love Calculater")

name1 = input("Whats your name? ")
name2 = input("Whats their name? ")

res = name1+name2
res = res.lower()

t = res.count("t")
r = res.count("r")
u = res.count("u")
e = res.count("e")
true = t+r+u+e

l = res.count("l")
o = res.count("o")
v = res.count("v")
e = res.count("e")
love = l+o+v+e

love_score = str(true) + str(love)
# print(love_score)
int_sc = int(love_score)

if(int_sc < 10) or (int_sc > 90):
  print(f"Your Score is {love_score}, you go like coke and mentor")

elif (int_sc >= 40) and (int_sc <= 50):
  print(f"Your Score is {love_score}, you are alright together")

else:
  print(f"Your Score is {love_score}")


