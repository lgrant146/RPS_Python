# Write your code here
import random

choice = input()

rps = ['rock', 'paper', 'scissors']

computer_choice = random.choice(rps)

win = {'rock': 'scissors',
       'scissors': 'paper',
       'paper': 'rock'
       }
lose = {'rock': 'paper',
        'scissors': 'rock',
        'paper': 'scissors'
        }

if choice == computer_choice:
    print("There is a draw (" + computer_choice + ")")
elif win[choice] == computer_choice:
    print("Well done. The computer chose " + computer_choice + " and failed")
elif lose[choice] == computer_choice:
    print(f"Sorry, but the computer chose {computer_choice}")
