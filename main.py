# my class imports
from classes.TurnsClass import HandleTurns

# init basic variables for the game
player = input("Which player would you like to be? [1 or 2] ")

# start game
startGame = HandleTurns(player)