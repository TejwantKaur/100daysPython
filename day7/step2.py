import random

word_list = ["ardvark", "baboon", "camel"]
choice = random.choice(word_list)

# Testing code
print(f"Pssst, the solution is {choice} ")

# blanks
empty_list = []
# for letter in choice:
word_length = len(choice)
for _ in range(word_length):
  empty_list += "_"
print(empty_list)

# input from user
guess = input("\nGuess a letter: ").lower()

for position in range(word_length):
  letter = choice[position]
  if(letter == guess):
    empty_list[position] = letter

print(empty_list)
  

