##
#
# Author: VishGit1234
# Date 11/2/2020
#
import random
from random import randint

# These are the possible choices in the game, using the randint function, the computer will be a choice based on the integer it chooses
list = ['rock', 'paper', 'scissors', 'spock', 'lizard']

# Assign a random valid choice to computerChoice (computer answer)
computerChoice = list[randint(0, 2)]

# Get user input and store
isValid = False
while isValid == False:
    print('Input one of the following; rock, paper, scissors, spock or lizard')
    Choice = input()
    Choice = Choice.lower()
    for i in list:
        if Choice == i:
            isValid = True
    if isValid == False:
        print(Choice + ' is an incorrect input')

# Compare Choice and computerChoice to see who wins

# The following is all the comparisons if the computer chooses "Rock"
if computerChoice == 'rock' and Choice == 'scissors':
    print('You chose ' + Choice + ' and the computer chose ' +
          computerChoice + ', The computer wins!')

elif computerChoice == 'rock' and Choice == 'paper':
    print('You chose ' + Choice + ' and the computer chose ' +
          computerChoice + ', You win!')

elif computerChoice == 'rock' and Choice == 'spock':
    print('You chose ' + Choice + ' and the computer chose ' +
          computerChoice + ', You win!')

elif computerChoice == 'rock' and Choice == 'lizard':
    print('You chose ' + Choice + ' and the computer chose ' +
          computerChoice + ', The computer wins!')
    
# The following is all the comparisons if the computer chooses "Paper"
elif computerChoice == 'paper' and Choice == 'rock':
    print('You chose ' + Choice + ' and the computer chose ' +
          computerChoice + ', The computer wins!')

elif computerChoice == 'paper' and Choice == 'scissors':
    print('You chose ' + Choice + ' and the computer chose ' +
          computerChoice + ', You win!')

elif computerChoice == 'paper' and Choice == 'spock':
    print('You chose ' + Choice + ' and the computer chose ' +
          computerChoice + ', The computer wins!')

elif computerChoice == 'paper' and Choice == 'lizard':
    print('You chose ' + Choice + ' and the computer chose ' +
          computerChoice + ', You win!')

# The following is all the comparisons if the computer chooses "Scissors"
elif computerChoice == 'scissors' and Choice == 'paper':
    print('You chose ' + Choice + ' and the computer chose ' +
          computerChoice + ', The computer wins!')

elif computerChoice == 'scissors' and Choice == 'rock':
    print('You chose ' + Choice + ' and the computer chose ' +
          computerChoice + ', You win!')

elif computerChoice == 'scissors' and Choice == 'spock':
    print('You chose ' + Choice + ' and the computer chose ' +
          computerChoice + ', You win!')

elif computerChoice == 'scissors' and Choice == 'lizard':
    print('You chose ' + Choice + ' and the computer chose ' +
          computerChoice + ', The computer wins!')

# The case in which both the computer and the user chose the same one, and they tie
else:
    print('You chose ' + Choice + ' and the computer chose ' +
          computerChoice + ', you tied!')
