##
#
# Author: FX Coding Club
#
# Edited by Luke Sequeira
#
# Date 9/24/2020
#

#
# 1 => rock
# 2 => paper
# 3 => scissors
#
#

import random


# These are the possible choices in the game, using the randint function, the computer will be a choice based on the integer it chooses
list = ['rock', 'paper', 'scissors']
random.seed()
computerChoice = random.randint(1, 3)

#get a text value from the int chosen
if(computerChoice == 1):
    comptext = "rock"
if(computerChoice == 2):
    comptext = "paper"
if(computerChoice == 3):
    comptext = "scissors"

playerChoice = input("Choose rock, paper or scisors\n>>> ")
tc = playerChoice[0]
if(tc != 's' and tc != 'r' and tc != 'p'):
    print("Please enter something begining with r, p or s (roc is ok but not ock)")
    playerChoice = input("Choose rock, paper or scisors\n>>> ")

# Compare playerChoice and computerChoice to see who wins

# The following is all the comparisons if the computer chooses "Rock"
if (computerChoice == 1 and playerChoice[0] == 's'):
    print('You chose ' + playerChoice + ' and the computer chose ' +
          comptext + ', The computer wins!')

elif (computerChoice == 1 and playerChoice[0] == 'p'):
    print('You chose ' + playerChoice + ' and the computer chose ' +
          comptext + ', You win!')

# The following is all the comparisons if the computer chooses "Paper"
elif (computerChoice == 2 and playerChoice[0] == 'r'):
    print('You chose ' + playerChoice + ' and the computer chose ' +
          comptext + ', The computer wins!')

elif (computerChoice == 2 and playerChoice[0] == 's'):
    print('You chose ' + playerChoice + ' and the computer chose ' +
          comptext + ', You win!')

# The following is all the comparisons if the computer chooses "Scissors"
elif (computerChoice == 3 and playerChoice[0] == 'p'):
    print('You chose ' + playerChoice + ' and the computer chose ' +
          comptext + ', The computer wins!')

elif (computerChoice == 3 and playerChoice[0] == 'r'):
    print('You chose ' + playerChoice + ' and the computer chose ' +
          comptext + ', You win!')

# The case in which both the computer and the user chose the same one, and they tie
else:
    print('You chose ' + str(playerChoice) + ' and the computer chose ' +
          comptext + ', you tied!')
