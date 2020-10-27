##
#
# Author: FX Coding Club
# Date 9/24/2020
#

import random

# These are the possible choices in the game, using the randint function, the computer will be a choice based on the integer it chooses
ls = ['rock', 'scissors', 'paper']

difficulty = 1 # chance for computer to win
playerChoice = input("Choose 'rock', 'paper' or 'scissors'")

nls = ls.copy()
nls.remove(playerChoice)

computerChoice = ""

if difficulty*100 == int(random.randrange(0, 100)):
    computerChoice = random.choice(nls)
else:
    computerChoice = ls[ls.index(playerChoice) - 1]
# Compare playerChoice and computerChoice to see who wins

# The following is all the comparisons if the computer chooses "Rock"
if computerChoice == 'rock' and playerChoice == 'scissors':
    print('You chose ' + playerChoice + ' and the computer chose ' +
          computerChoice + ', The computer wins!')

elif computerChoice == 'rock' and playerChoice == 'paper':
    print('You chose ' + playerChoice + ' and the computer chose ' +
          computerChoice + ', You win!')

# The following is all the comparisons if the computer chooses "Paper"
elif computerChoice == 'paper' and playerChoice == 'rock':
    print('You chose ' + playerChoice + ' and the computer chose ' +
          computerChoice + ', The computer wins!')

elif computerChoice == 'paper' and playerChoice == 'scissors':
    print('You chose ' + playerChoice + ' and the computer chose ' +
          computerChoice + ', You win!')

# The following is all the comparisons if the computer chooses "Scissors"
elif computerChoice == 'scissors' and playerChoice == 'paper':
    print('You chose ' + playerChoice + ' and the computer chose ' +
          computerChoice + ', The computer wins!')

elif computerChoice == 'scissors' and playerChoice == 'rock':
    print('You chose ' + playerChoice + ' and the computer chose ' +
          computerChoice + ', You win!')

# The case in which both the computer and the user chose the same one, and they tie
else:
    print('You chose ' + playerChoice + ' and the computer chose ' +
          computerChoice + ', you tied!')