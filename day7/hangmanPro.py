import random

word_list = ["ardvark", "baboon", "camel"]

# choose word
choice = random.choice(word_list)

# input from user
guess = input("Guess a letter: ").lower()

for letter in choice :
  if letter == guess:
    print("Right")
  else:
    print("Wrong")

