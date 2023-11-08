dict={
  "var1" : 'Hello',
  123: "Numberr"
}

print(dict[123])
print(dict["var1"])

dict[344] = "new added"
print(dict)

# edit 
dict[123] = "jabf"
print(dict)

# loop
for i in dict :
  print(i)
  print(dict[i])

# wipe dictionary
dict = {}
print(dict)