##
#
# Author: FX Coding Club
# Contributor: Jonathan Polina
# Date 9/27/2020
#
import random

# These are the possible choices in the game, using the randint function, the computer will be a choice based on the
# integer it chooses
list = ['rock', 'paper', 'scissors', 'spock', 'lizard']
computerChoice = list[random.randint(0, 4)]
choiceIsValid = False
choice = ''
while not choiceIsValid:
    choice = input("Please enter your choice: ")
    choice = choice.lower()
    # iterates through the options and switches choiceIsValid to true if a match is found
    for i in list:
        if choice == i:
            choiceIsValid = True
    if not choiceIsValid:
        print("Your choice is not valid. Try again.")


# create the win and lose message functions
def win_message():
    print('You chose ' + choice + ' and the computer chose ' + computerChoice + '. You win!')


def lose_message():
    print('You chose ' + choice + ' and the computer chose ' + computerChoice + '. The computer wins!')


# Compare choice and computerChoice to see who wins

# The following is all the comparisons if the computer chooses "rock"
if computerChoice == 'rock':
    if choice == 'spock' or choice == 'paper':
        win_message()
    elif choice == 'lizard' or choice == 'scissors':
        lose_message()

# The following is all the comparisons if the computer chooses "paper"
elif computerChoice == 'paper':
    if choice == 'lizard' or choice == 'scissors':
        win_message()
    elif choice == 'spock' or choice == 'rock':
        lose_message()


# The following is all the comparisons if the computer chooses "scissors"
elif computerChoice == 'scissors':
    if choice == 'spock' or choice == 'rock':
        win_message()
    elif choice == 'lizard' or choice == 'paper':
        lose_message()


# The following is all the comparisons if the computer chooses "spock"
elif computerChoice == 'spock':
    if choice == 'paper' or choice == 'lizard':
        win_message()
    elif choice == 'rock' or choice == 'scissors':
        lose_message()


# The following is all the comparisons if the computer chooses "lizard"
elif computerChoice == 'lizard':
    if choice == 'scissors' or choice == 'rock':
        win_message()
    elif choice == 'spock' or choice == 'paper':
        lose_message()


# The case in which both the computer and the user chose the same one, and they tie
if computerChoice == choice:
    print('You chose ' + choice + ' and the computer chose ' +
          computerChoice + ', you tied!')
