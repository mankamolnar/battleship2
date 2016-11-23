# my class imports
import tkinter as tk
from classes.GuiClass import Gui
from classes.SocketClass import Socket, ServerSocket, ClientSocket

root = tk.Tk()
app = Gui(root)
app.mainloop()
