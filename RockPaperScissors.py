##
#
# Author: FX Coding Club
# Date 9/24/2020
#
import random

#Implement a user input that verify whether the input made by the user is valid
playerInput = input("rock, paper, scissors, lizard, spock?\n")

# These are the possible choices in the game, using the randint function, the computer will be a choice based on the integer it chooses
list = ['rock', 'paper', 'scissors', 'lizard', 'spock']

#Adding Random for computer
computerChoice = random.choice(list)


# The following is all the comparisons if the computer chooses "Rock"

if (computerChoice == 'rock' and playerInput == 'scissors'):
        print('You chose ' + playerInput + ' and the computer chose ' + computerChoice + ', The computer wins!')
        
elif (computerChoice == 'rock' and playerInput == 'paper'):
        print('You chose ' + playerInput + ' and the computer chose ' + computerChoice + ', You win!')
        
elif (computerChoice == 'rock' and playerInput == 'lizard'):
        print('You chose ' + playerInput + ' and the computer chose ' + computerChoice + ', The computer wins!')

elif (computerChoice =='rock' and playerInput == 'spock'):
        print('You chose ' + playerInput + ' and the computer chose ' + computerChoice + ', You Win!')

    # The following is all the comparisons if the computer chooses "Paper"
elif (computerChoice == 'paper' and playerInput == 'rock'):
        print('You chose ' + playerInput + ' and the computer chose ' + computerChoice + ', The computer wins!')
        
elif (computerChoice == 'paper' and playerInput == 'scissors'):
        print('You chose ' + playerInput + ' and the computer chose ' + computerChoice + ', You win!')

elif (computerChoice =='paper' and playerInput == 'spock'):
        print('You chose ' + playerInput + ' and the computer chose ' + computerChoice + ', You The Computer Wins!')

elif (computerChoice =='paper' and playerInput == 'lizard'):
        print('You chose ' + playerInput + ' and the computer chose ' + computerChoice + ', You Win!')
        
    # The following is all the comparisons if the computer chooses "Scissors"
elif (computerChoice == 'scissors' and playerInput == 'paper'):
        print('You chose ' + playerInput + ' and the computer chose ' + computerChoice + ', The computer wins!')

elif (computerChoice == 'scissors' and playerInput == 'rock'):
        print('You chose ' + playerInput + ' and the computer chose ' + computerChoice + ', You win!')

elif (computerChoice =='scissors' and playerInput == 'lizard'):
        print('You chose ' + playerInput + ' and the computer chose ' + computerChoice + ', You win!')

elif (computerChoice =='scissors' and playerInput == 'spock'):
        print('You chose ' + playerInput + ' and the computer chose ' + computerChoice + ', You The Computer Wins!')

    # The case is all the comparison if the computer chooses "Lizard"
elif (computerChoice == 'lizard' and playerInput == 'paper'):
        print('You chose ' + playerInput + ' and the computer chose ' + computerChoice + ', The computer wins!')

elif (computerChoice == 'lizard' and playerInput == 'rock'):
        print('You chose ' + playerInput + ' and the computer chose ' + computerChoice + ', You win!')

elif (computerChoice =='lizard' and playerInput == 'scissors'):
        print('You chose ' + playerInput + ' and the computer chose ' + computerChoice + ', You win!')

elif (computerChoice =='lizard' and playerInput == 'spock'):
        print('You chose ' + playerInput + ' and the computer chose ' + computerChoice + ', The Computer Wins!')

 # The case is all the comparison if the computer chooses "Spock"
elif (computerChoice == 'spock' and playerInput == 'paper'):
        print('You chose ' + playerInput + ' and the computer chose ' + computerChoice + ', You win!')

elif (computerChoice == 'spock' and playerInput == 'rock'):
        print('You chose ' + playerInput + ' and the computer chose ' + computerChoice + ', The computer wins!')

elif (computerChoice =='spock' and playerInput == 'scissors'):
        print('You chose ' + playerInput + ' and the computer chose ' + computerChoice + ', The computer wins!')

elif (computerChoice =='spock' and playerInput == 'lizard'):
        print('You chose ' + playerInput + ' and the computer chose ' + computerChoice + ', You win!')
    # The case in which both the computer and the user chose the same one, and they tie
else:
        print('You chose ' + playerInput + ' and the computer chose ' + computerChoice + ', you tied!')
