#!/usr/bin/python3
import math
import random
import sys

class Player:

    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            print(self.letter + '\'s turn Input move (0-8):')
            val = sys.stdin.readline().strip()
            try:
                move = int(val)
                if move not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid move. Try again.')
        return move
