# my class imports
import tkinter as tk
from classes.GuiClass import Gui

# init basic variables for the game
# player = input("Which player would you like to be? [1 or 2] ")

# start game
# startGame = HandleTurns(player)


root = tk.Tk()
app = Gui(root)
app.mainloop()
