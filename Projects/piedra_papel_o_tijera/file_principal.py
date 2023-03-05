#!/usr/bin/python3
import random 
     
def play():

    print("Welcome to Rock, Paper, Scissors Game")

    user = input(" What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user, computer):
         return 'You won!'
    
    else:
         return 'You lost'

def is_win(player, opponent):
     
     if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
        or (player == 'p' and opponent == 'r'):
         return True

print(play())