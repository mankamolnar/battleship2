import tkinter as tk
from classes.TurnsClass import HandleTurns
import os
import _thread


class Gui(tk.Frame):

    root = ""
    bg = ""
    widgets = []
    turns = ""

    def __init__(self, master=None):
        super().__init__(master)
        self.root = master
        self.start_main()

    # !!! GAME SCREENS !!!
    # MAIN MENU: load in the needed modules for the main screen
    def start_main(self):
        self.configure_window()
        self.main_widgets()

    # MAIN MENU: placing buttons on main
    def main_widgets(self):
        self.widget_logo()
        self.widget_host_button()
        self.widget_client_button()
        self.widget_new_window_button()
        #self.widget_quit_button()

    # HOST MENU: main widgets
    def host_widgets(self):
        self.clear_widgets()
        self.widget_logo()
        self.widget_label_sublogo("Waiting to connect by someone")
        self.widget_quit_button()

    # CLIENT MENU: main widgets
    def client_widgets(self):
        self.clear_widgets()
        self.widget_logo()
        self.widget_label_sublogo("Write in the host's IP!")
        self.widget_ip_input()
        self.widget_connect_button()
        self.widget_quit_button()

    # CLIENT MENU: connection refused
    def client_on_error_widgets(self):
        self.clear_widgets()
        self.widget_logo()
        self.widget_label_sublogo("Couldn't connect to this IP!")
        self.widget_ip_input()
        self.widget_connect_button()
        self.widget_quit_button()


    # !!! WIDGETS !!!
    # place logo
    def widget_logo(self):
        tmp_img = tk.PhotoImage(file=self.getAbsPath()+"../battleshipLogo.gif")
        self.widgets.append(tk.Label(self.root, image=tmp_img))
        self.widgets[len(self.widgets)-1].img = tmp_img
        self.widgets[len(self.widgets)-1].place(relx=0.5, y=5, x=-200)

    # host button
    def widget_host_button(self):
        self.widgets.append(tk.Button(self.root))
        self.widgets[len(self.widgets)-1]["text"] = "Host"
        self.widgets[len(self.widgets)-1]["command"] = self.start_turns_player_1
        self.widgets[len(self.widgets)-1]["width"] = 10
        self.widgets[len(self.widgets)-1]["height"] = 3
        self.widgets[len(self.widgets)-1].place(relx=0.5, y=155, x=-50)

    # client button
    def widget_client_button(self):
        self.widgets.append(tk.Button(self.root))
        self.widgets[len(self.widgets)-1]["text"] = "Client"
        self.widgets[len(self.widgets)-1]["command"] = self.client_widgets
        self.widgets[len(self.widgets)-1]["width"] = 10
        self.widgets[len(self.widgets)-1]["height"] = 3
        self.widgets[len(self.widgets)-1].place(relx=0.5, y=285, x=-50)

    # quit button
    def widget_quit_button(self):
        self.widgets.append(tk.Button(self.root))
        self.widgets[len(self.widgets)-1]["text"] = "Quit"
        self.widgets[len(self.widgets)-1]["fg"] = "Red"
        self.widgets[len(self.widgets)-1]["activeforeground"] = "Red"
        self.widgets[len(self.widgets)-1]["width"] = 10
        self.widgets[len(self.widgets)-1]["height"] = 3
        self.widgets[len(self.widgets)-1]["command"] = self.root.destroy
        self.widgets[len(self.widgets)-1].place(relx=0.5, y=415, x=-50)

    # waiting for connection
    def widget_label_sublogo(self, ptext):
        self.widgets.append(tk.Label(self.root, text=ptext, width=40, fg="Red"))
        self.widgets[len(self.widgets)-1].place(relx=0.5, x=-160, y=110)

    # ip entry
    def widget_ip_input(self):
        self.widgets.append(tk.Entry(self.root, width=20))
        self.widgets[len(self.widgets)-1].place(relx=0.5, x=-80, y=133)

    # connect to host button
    def widget_connect_button(self):
        self.widgets.append(tk.Button(self.root))
        self.widgets[len(self.widgets)-1]["text"] = "Connect"
        self.widgets[len(self.widgets)-1]["width"] = 10
        self.widgets[len(self.widgets)-1]["height"] = 3
        self.widgets[len(self.widgets)-1]["command"] = self.start_turns_player_2
        self.widgets[len(self.widgets)-1].place(relx=0.5, y=156, x=-50)

    # new window button
    def widget_new_window_button(self):
        self.widgets.append(tk.Button(self.root))
        self.widgets[len(self.widgets)-1]["text"] = "New window"
        self.widgets[len(self.widgets)-1]["width"] = 10
        self.widgets[len(self.widgets)-1]["height"] = 3
        self.widgets[len(self.widgets)-1]["command"] = self.new_window
        self.widgets[len(self.widgets)-1].place(relx=0.5, y=415, x=-50)

    # set window size and place bg image
    def configure_window(self):
        self.root.minsize(width=800, height=600)
        self.bgimg = tk.PhotoImage(file=self.getAbsPath()+"../bg.gif")
        self.bg = tk.Label(self.root, image=self.bgimg)
        self.bg.img = self.bgimg
        self.bg.place(x=0, y=0, relwidth=1, relheight=1)

    # empty the screen
    def clear_widgets(self):
        for widget in self.widgets:
            widget.place_forget()

    # !!! SYSTEM FUNCTIONS !!!
    # create turns class for player 1
    def start_turns_player_1(self):
        self.host_widgets()
        _thread.start_new_thread(HandleTurns, (1, self, ))

    # create turns class for player 2
    def start_turns_player_2(self):
        ip = ""
        for widget in self.widgets:
            if type(widget) == tk.Entry:
                ip = widget.get()
        _thread.start_new_thread(HandleTurns, (2, self, ip, ))

    def say_hi(self):
        print("hi there, everyone!")

    def getAbsPath(self):
        return os.path.dirname(os.path.abspath(__file__))+"/"

    def new_window(self):
        #self.newWindow = tk.Toplevel(self.root)
        self.app = Gui(tk.Tk())
