def add(num1, num2):
  return num1+num2
def sub(n1, n2):
  return n1-n2
def mul(n1,n2):
  return n1*n2
def div(n1,n2):
  return n1/n2

operations = {
  "+" : add,
  "-" : sub,
  "*" : mul,
  "/" : div
}

num1 = float(input("Enter num1: "))
for op in operations:
  print(op)
sym = input("Enter operator: ")
num2 = float(input("Enter num2: "))

operator = operations[sym]
first_result = round(operator(num1,num2),3)

print(f"{num1} {sym} {num2} = {first_result} ")

# res = True
while True:
  resume = input("Want to continue? 'y' 'n' ")
  
  if resume == "n":
    res = False
    print("GoodBye")
    break
    
  sym = input("Pick another operator: ")
  num3 = float(input("What's the next num? "))

  operator = operations[sym]
  sec_result = round(operator(first_result,num3),3)
  
  print(f"{first_result} {sym} {num3} = {sec_result}")
  
  # res = False





