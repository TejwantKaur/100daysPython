import random

words = ["ardvark", "baboon", "camel"]
choice = random.choice(words)
print(f"Pssst, the solution is {choice} ")

display = []
word_length = len(choice)

for _ in range(word_length):
  display += "_"

print(display)
endOfGame = False
print()

lives = 6
while not endOfGame:
  guess = input("Guess a letter: ").lower()
  
  for position in range(word_length):
    letter = choice[position]
    if(letter == guess):
      display[position] = letter

  if guess not in display:
    lives -= 1
    if lives == 0:
      endOfGame=True
      print("You Lose")
    
  print(display)

  if '_' not in display:
    endOfGame = True
    print("You win")
  