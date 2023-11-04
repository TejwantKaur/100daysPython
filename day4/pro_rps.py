import random

# Rock
rock = ("""
    ______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)___
           ______)
          ________)
         ________)
---.___________)
""")

# Scissors
scissor = ("""
    _______
---'   ____)_____
          _______)
       ___________)
      (____)
---.__(___)
""")

choices = [rock,paper,scissor]

print("Welcome to Rock Paper Scissor!!")
print("Here are three choicesPress ")
user_choice = int(input(" 0 for 'Rock'\n 1 for'Paper'\n 2 for 'Scissors': "))

if(user_choice > 2 or user_choice < 0 ):
    print("You typed invalid number! you loose")

else:
    print("\nYou Choose: ")
    print(choices[user_choice])

    # compChoice = random.choice(choices)
    # print(compChoice)
    
    comp_choice = random.randint(0,2)
    print("\nComputer Choose: ")
    print(choices[comp_choice])


    if(user_choice == 0 and comp_choice == 2):
      print("You win")
        
    elif((comp_choice == 0 and user_choice == 2) or comp_choice > user_choice):
      print("You lose")

    elif(comp_choice < user_choice):
        print("You win")
    
    elif(comp_choice == user_choice):
        print("Draw")
    
    
    




