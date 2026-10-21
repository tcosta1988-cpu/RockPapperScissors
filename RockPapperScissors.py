rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

import random

#User Choice
your_choice = int(input("What do you choose?\n0 for Rock\n1 for Paper\n2 for Scissors\n"))
if your_choice >= 0 and your_choice <= 2:
    print(f"Your Choise is: {your_choice}")
    print(game_images[your_choice])

    #Computer Choice (Random)
    computer_choice = random.randint(0,2)
    print(f"Computer Choice: {computer_choice}")
    print(game_images[computer_choice])

#Game
if your_choice < 0 or your_choice >= 2:
    print("You choose a invalid number. You Lose")
else:
    if your_choice == computer_choice:
        print("Draw")
    elif your_choice == 0 and computer_choice == 1:
        print("You Lose")
    elif your_choice == 0 and computer_choice == 2:
        print("You Win")
    elif your_choice == 1 and computer_choice == 0:
        print("You Win")
    elif your_choice == 1 and computer_choice == 2:
        print("You Lose")
    elif your_choice == 2 and computer_choice == 0:
        print("You Lose")
    elif your_choice == 2 and computer_choice == 1:
        print("You Win")
