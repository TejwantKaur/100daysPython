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
result = round(operator(num1,num2),3)

print(f"{num1} {sym} {num2} = {result} ")
