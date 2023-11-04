import random

names = input("Enter names with comma: ")
names = names.split(",")

random = random.randint(0,len(names)-1)

print(names[random] + " will pay bill")