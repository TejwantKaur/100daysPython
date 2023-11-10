import random

lets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N', 'O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

sp_char = ['!','"','#','$','%','&',"'",'(',')','*','+','-','.','/',':', ';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~']

num_char = ['0','1','2','3','4','5','6','7','8','9']

print("Welcome to pyPassword Generator!!")
let = int (input("how many letters uh want to add? "))
sym = int (input("how many symbols uh want to add? "))
num = int (input("how many numbers uh want to add? "))

pass_list = [];
for ch in range (1, let+1):
  pass_list.append(random.choice(lets))

for ch in range (1, sym+1):
  pass_list.append(random.choice(sp_char))

for ch in range (1, num+1):
  pass_list.append(random.choice(num_char))

# print(pass_list)
random.shuffle(pass_list)
# print(pass_list)

password = ""

for char in pass_list:
  password += char

print(f"Your password is {password}")
  