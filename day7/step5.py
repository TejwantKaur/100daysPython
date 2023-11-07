import random

from hangman_words import words

choice = random.choice(words)
display = []
word_length = len(choice)

for _ in range(word_length):
  display += "_"
print(display)

endOfGame = False
lives = 6

from hangman_art import logo,stages

print(logo)

print()
while not endOfGame:
  guess = input("Guess a letter: ").lower()

  # already guessed
  if guess in display:
    print(f"You have already guessed {guess} ")
  for position in range(word_length):
    letter = choice[position]
    if(letter == guess):
      display[position] = letter

  if guess not in display:
    print(f"You guessed {guess} which is wrong, you lose a life ")
    lives -= 1
    if lives == 0:
      endOfGame=True
      print("You Lose")

  print(display)

  if '_' not in display:
    endOfGame = True
    print("You win")

  print(stages[lives])

print(f"Pssst, the solution is {choice} ")