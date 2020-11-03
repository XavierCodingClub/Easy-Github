##
#
# Author: FX Coding Club, Ethan Bhalla
# Date 11/03/2020
# Description: This code is an updated and skewed version of rock, paper, scissors!!

import random as rnd

# These are the possible choices in the game, using the randint function, the computer will be a choice based on the integer it chooses
choices = ['rock', 'paper', 'scissors', 'pistol', 'water', 'sourya']

playerChoice = ' '
computerChoices = rnd.choice(choices)

validatePlayerChoice = False

#Input validation to make sure there are no user errors when inputting a choice
while not validatePlayerChoice:
    playerChoice = str(input("Please enter your choice, choose between Rock, Paper, Scissors, Pistol, Sourya: ")).lower()
    if playerChoice in choices:
        validatePlayerChoice = True
    else:
        print("Please try again, make sure you spell everything correctly")

# Compare playerChoice and computerChoice to see who wins

# The following is all the comparisons if the computer chooses "Rock"
if computerChoices == 'rock' and playerChoice == 'scissors':
    print('You chose ' + playerChoice + ' and the computer chose ' + computerChoices + ', The computer wins!')

elif computerChoices == 'rock' and playerChoice == 'paper':
    print('You chose ' + playerChoice + ' and the computer chose ' + computerChoices + ', You win!')

elif computerChoices == 'rock' and playerChoice == 'pistol':
    print('You chose ' + playerChoice + ' and the computer chose ' + computerChoices + ', The computer wins!')

elif computerChoices == 'rock' and playerChoice == 'water':
    print('You chose ' + playerChoice + ' and the computer chose ' + computerChoices + ', The player wins!')

elif computerChoices == 'rock' and playerChoice == 'sourya':
    print('You chose ' + playerChoice + ' and the computer chose ' + computerChoices + ', You win! Sourya always win!')

#----------------------------------------------------------------------------------------------------
# The following is all the comparisons if the computer chooses "Paper"
elif computerChoices == 'paper' and playerChoice == 'rock':
    print('You chose ' + playerChoice + ' and the computer chose ' + computerChoices + ', The computer wins!')

elif computerChoices == 'paper' and playerChoice == 'scissors':
    print('You chose ' + playerChoice + ' and the computer chose ' + computerChoices + ', You win!')

elif computerChoices == 'paper' and playerChoice == 'pistol':
    print('You chose ' + playerChoice + ' and the computer chose ' + computerChoices + ', You win!')

elif computerChoices == 'paper' and playerChoice == 'water':
    print('You chose ' + playerChoice + ' and the computer chose ' + computerChoices + ', The computer wins!')

elif computerChoices == 'paper' and playerChoice == 'sourya':
    print('You chose ' + playerChoice + ' and the computer chose ' + computerChoices + ', You win! Sourya always wins!')

#----------------------------------------------------------------------------------------------------
# The following is all the comparisons if the computer chooses "Scissors"
elif computerChoices == 'scissors' and playerChoice == 'paper':
    print('You chose ' + playerChoice + ' and the computer chose ' + computerChoices + ', The computer wins!')

elif computerChoices == 'scissors' and playerChoice == 'rock':
    print('You chose ' + playerChoice + ' and the computer chose ' + computerChoices + ', You win!')

elif computerChoices == 'scissors' and playerChoice == 'pistol':
    print('You chose ' + playerChoice + ' and the computer chose ' + computerChoices + ', You Win!')

elif computerChoices == 'scissors' and playerChoice == 'water':
    print('You chose ' + playerChoice + ' and the computer chose ' + computerChoices + ', The computer wins!')

elif computerChoices == 'scissors' and playerChoice == 'sourya':
    print('You chose ' + playerChoice + ' and the computer chose ' + computerChoices + ', You Win! Sourya always win')

#----------------------------------------------------------------------------------------------------
# The following is all the comparisons if the computer chooses "Pistol"
elif computerChoices == 'pistol' and playerChoice == 'rock':
    print('You chose' + playerChoice + ' and the computer chose' + computerChoices + ', You Win!')

elif computerChoices == 'pistol' and playerChoice == 'paper':
    print('You chose' + playerChoice + 'and the computer chose' + computerChoices + 'The Computer wins!')

elif computerChoices == 'pistol' and playerChoice == 'scissors':
    print('You chose' + playerChoice + 'and the computer chose' + computerChoices + ',  The computer Wins!')

elif computerChoices == 'pistol' and playerChoice == 'water':
    print('You chose' + playerChoice + 'and the computer chose' + computerChoices + ', You Win')

elif computerChoices == 'pistol' and playerChoice == 'sourya':
    print('You chose' + playerChoice + 'and the computer chose' + computerChoices + ', You Win! Sourya always wins')

#----------------------------------------------------------------------------------------------------
#The following is all the comparisons if the computer chooses "Water"

elif computerChoices == 'water' and playerChoice == 'rock':
    print('You chose' + playerChoice + ' and the computer chose' + computerChoices + ', The computer wins!')

elif computerChoices == 'water' and playerChoice == 'paper':
    print('You chose' + playerChoice + ' and the computer chose' + computerChoices + ', You Win!')

elif computerChoices == 'water' and playerChoice == 'scissors':
    print('You chose' + playerChoice + ' and the computer chose' + computerChoices + ', The computer wins!')

elif computerChoices == 'water' and playerChoice == 'rock':
    print('You chose' + playerChoice + ' and the computer chose' + computerChoices + ', The computer wins!')

elif computerChoices == 'water' and playerChoice == 'sourya':
    print('You chose' + playerChoice + ' and the computer chose' + computerChoices + ', You Win! Sourya always wins!')

#----------------------------------------------------------------------------------------------------
#The following us all the comparisons if the computer chooses "Sourya"

elif computerChoices == 'sourya' and playerChoice == 'rock':
    print('You chose' + playerChoice + ' and the computer chose' + computerChoices + ', The computer wins! Sourya always wins')

elif computerChoices == 'sourya' and playerChoice == 'paper':
    print('You chose' + playerChoice + ' and the computer chose' + computerChoices + ', The computer wins! Sourya always wins')

elif computerChoices == 'sourya' and playerChoice == 'scissors':
    print('You chose' + playerChoice + ' and the computer chose' + computerChoices + ', The computer wins! Sourya always wins')

elif computerChoices == 'sourya' and playerChoice == 'pistol':
    print('You chose' + playerChoice + ' and the computer chose' + computerChoices + ', The computer wins! Sourya always wins')

elif computerChoices == 'sourya' and playerChoice == 'water':
    print('You chose' + playerChoice + ' and the computer chose' + computerChoices + ', The computer wins! Sourya always wins')

#----------------------------------------------------------------------------------------------------
# The case in which both the computer and the user chose the same one, and they tie
else:
    print('You chose ' + playerChoice + ' and the computer chose ' + computerChoices + ', you tied!')
