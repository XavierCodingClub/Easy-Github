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
from libs import playsound

sound = True

score = 0 # Scores and
games = 0 # Game played

foo = input("Play with sound? y or n (if you do not choose a valid option, y is selected by default)")
if(foo == 'n'):
    sound = False
    print("Sound has been turned off")

print("Welcome to Rock-Paper-Scissors. Type end anytime to exit.")
def game():

    global score
    global games
    global sound
    
    games += 1
    
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
    if(playerChoice == 'end'):
        print("Ending Game, We'll miss you!")
        exit()
    if(playerChoice == 'cheat'):
        score += int(input("How much do you want to add to you score? "));
        game()
        
    tc = playerChoice[0]
    if(tc != 's' and tc != 'r' and tc != 'p'):
        print("Please enter something begining with r, p or s (roc is ok but not ock)")
        playerChoice = input("Choose rock, paper or scisors\n>>> ")

    # Compare playerChoice and computerChoice to see who wins

    # The following is all the comparisons if the computer chooses "Rock"
    if (computerChoice == 1 and playerChoice[0] == 's'):
        print('You chose ' + playerChoice + ' and the computer chose ' +
            comptext + ', The computer wins!')
        if(sound):
            playsound.playsound("boo.wav")

    elif (computerChoice == 1 and playerChoice[0] == 'p'):
        print('You chose ' + playerChoice + ' and the computer chose ' +
              comptext + ', You win!')
        score += 1
        if(sound):
            playsound.playsound("correct_answer_music.mp3")
            
    # The following is all the comparisons if the computer chooses "Paper"
    elif (computerChoice == 2 and playerChoice[0] == 'r'):
        print('You chose ' + playerChoice + ' and the computer chose ' +
              comptext + ', The computer wins!')
        if(sound):
            playsound.playsound("boo.wav")

    elif (computerChoice == 2 and playerChoice[0] == 's'):
        print('You chose ' + playerChoice + ' and the computer chose ' +
              comptext + ', You win!')
        score += 1
        if(sound):
            playsound.playsound("correct_answer_music.mp3")

    # The following is all the comparisons if the computer chooses "Scissors"
    elif (computerChoice == 3 and playerChoice[0] == 'p'):
        print('You chose ' + playerChoice + ' and the computer chose ' +
              comptext + ', The computer wins!')
        score += 1
        if(sound):
            playsound.playsound("boo.wav")

    elif (computerChoice == 3 and playerChoice[0] == 'r'):
        print('You chose ' + playerChoice + ' and the computer chose ' +
              comptext + ', You win!')
        score += 1
        if(sound):
            playsound.playsound("correct_answer_music.mp3")
            
    # The case in which both the computer and the user chose the same one, and they tie
    else:
        print('You chose ' + str(playerChoice) + ' and the computer chose ' +
              comptext + ', you tied!')
        score += 0.5
    print("You've won " + str(score) + " out of " + str(games) + " games (draws count as 0.5). That is a " + str(score/games * 100) + "% avergage!")
    game()
    
game()
    
