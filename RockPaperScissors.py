##
#
# Author: FX Coding Club
# Date 9/24/2020
#


# These are the possible choices in the game, using the randint function, the computer will be a choice based on the integer it chooses
list = ['rock', 'paper', 'scissors','lizard','spock']


# Compare var1 and computerChoice to see who wins

# The following is all the comparisons if the computer chooses "Rock"
if computerChoice == 'rock' and var1 == 'scissors'):
    print('You chose ' + var1 + ' and the computer chose ' + computerChoice + ', The computer wins!')

elif computerChoice == 'rock' and var1 == 'paper'):
    print('You chose ' + var1 + ' and the computer chose ' +
          computerChoice + ', You win!')

elif computerChoice == 'rock' and var1 == 'lizard'):
    print('You chose ' + var1 + ' and the computer chose ' +
          computerChoice + ', The computer wins!')

elif computerChoice == 'rock' and var1 == 'spock'):
    print('You chose ' + var1 + ' and the computer chose ' +
          computerChoice + ', You win!')

# The following is all the comparisons if the computer chooses "Paper"
elif computerChoice == 'paper' and var1 == 'rock'):
    print('You chose ' + var1 + ' and the computer chose ' +
          computerChoice + ', The computer wins!')

elif computerChoice == 'paper' and var1 == 'scissors'):
    print('You chose ' + var1 + ' and the computer chose ' +
          computerChoice + ', You win!')

elif computerChoice == 'paper' and var1 == 'spock'):
    print('You chose ' + var1 + ' and the computer chose ' +
          computerChoice + ', The computer wins!')

elif computerChoice == 'paper' and var1 == 'lizard'):
    print('You chose ' + var1 + ' and the computer chose ' +
          computerChoice + ', You win!')

# The following is all the comparisons if the computer chooses "Scissors"
elif computerChoice == 'scissors' and var1 == 'paper'):
    print('You chose ' + var1 + ' and the computer chose ' +
          computerChoice + ', The computer wins!')

elif computerChoice == 'scissors' and var1 == 'rock'):
    print('You chose ' + var1 + ' and the computer chose ' +
          computerChoice + ', You win!')

elif computerChoice == 'scissors' and var1 == 'lizard'):
    print('You chose ' + var1 + ' and the computer chose ' +
          computerChoice + ', The computer wins!')

elif computerChoice == 'scissors' and var1 == 'spock'):
    print('You chose ' + var1 + ' and the computer chose ' +
          computerChoice + ', You win!')

#spock rules

elif computerChoice == 'spock' and var1 == 'scissors'):
    print('You chose ' + var1 + ' and the computer chose ' +
          computerChoice + ', The computer wins!')

elif computerChoice == 'spock' and var1 == 'paper'):
    print('You chose ' + var1 + ' and the computer chose ' +
          computerChoice + ', You win!')

elif computerChoice == 'spock' and var1 == 'rock'):
    print('You chose ' + var1 + ' and the computer chose ' +
          computerChoice + ', The computer wins!')

elif computerChoice == 'spock' and var1 == 'lizard'):
    print('You chose ' + var1 + ' and the computer chose ' +
          computerChoice + ', You win!')

#Lizard rules

elif computerChoice == 'lizard' and var1 == 'spock'):
    print('You chose ' + var1 + ' and the computer chose ' +
          computerChoice + ', The computer wins!')

elif computerChoice == 'lizard' and var1 == 'rock'):
    print('You chose ' + var1 + ' and the computer chose ' +
          computerChoice + ', You win!')

elif computerChoice == 'lizard' and var1 == 'paper'):
    print('You chose ' + var1 + ' and the computer chose ' +
          computerChoice + ', The computer wins!')

elif computerChoice == 'lizard' and var1 == 'scissors'):
    print('You chose ' + var1 + ' and the computer chose ' +
          computerChoice + ', You win!')

# The case in which both the computer and the user chose the same one, and they tie
else:
    print('You chose ' + var1 + ' and the computer chose ' +
          computerChoice + ', you tied!')
