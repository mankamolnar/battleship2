import tkinter as tk
from classes.TurnsClass import HandleTurns
import os
import _thread


class Gui(tk.Frame):

    root = ""
    bg = ""
    widgets = []
    turns = ""
    horizontal_or_vertical = "H"

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
        self.widget_quit_button()

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

    # PLACE SHIPS
    def place_ships_widgets(self, map=""):
        self.clear_widgets()
        self.widget_logo()
        self.widget_label_sublogo("Where would you like to place your "+str(self.turns.all_ships[self.turns.current_ship])+" long ship!")
        self.widget_coo_input()
        self.widget_horizontal_or_vertical_radio()
        self.widget_place_ship_button()
        self.widget_print_map(self.turns.map.myMap)

    def error_on_place_ships_widgets(self, map=""):
        self.clear_widgets()
        self.widget_logo()
        self.widget_label_sublogo("You cannot place your "+str(self.turns.all_ships[self.turns.current_ship])+" long ship there! Try again!")
        self.widget_coo_input()
        self.widget_horizontal_or_vertical_radio()
        self.widget_place_ship_button()
        self.widget_print_map(self.turns.map.myMap)

    def waiting_for_enemy_to_place_ships_with_map(self, map=""):
        self.clear_widgets()
        self.widget_logo()
        self.widget_label_sublogo("Waiting for your enemy to place his ships!")
        self.widget_print_map(self.turns.map.myMap)

    def waiting_for_enemy_to_place_ships(self):
        self.clear_widgets()
        self.widget_logo()
        self.widget_label_sublogo("Waiting for enemy to place his ships!")
        self.widget_quit_button()

    def shoot_widgets(self):
        self.clear_widgets()
        self.widget_logo()
        self.widget_label_sublogo("Write in where would you like to shoot!")
        self.widget_coo_input()
        self.widget_print_map(self.turns.map.shotMap)
        self.widget_shoot_button()
        self.widget_show_life()

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

    # Place Ship button
    def widget_place_ship_button(self):
        self.widgets.append(tk.Button(self.root))
        self.widgets[len(self.widgets)-1]["text"] = "Place ship!"
        self.widgets[len(self.widgets)-1]["width"] = 10
        self.widgets[len(self.widgets)-1]["height"] = 3
        self.widgets[len(self.widgets)-1]["command"] = self.handle_placeship
        self.widgets[len(self.widgets)-1].place(relx=0.5, y=485, x=-50)

    def widget_shoot_button(self):
        self.widgets.append(tk.Button(self.root))
        self.widgets[len(self.widgets)-1]["text"] = "Shoot!"
        self.widgets[len(self.widgets)-1]["width"] = 10
        self.widgets[len(self.widgets)-1]["height"] = 3
        self.widgets[len(self.widgets)-1]["command"] = self.handle_shoot
        self.widgets[len(self.widgets)-1].place(relx=0.5, y=485, x=-50)

    # waiting for connection
    def widget_label_sublogo(self, ptext):
        self.widgets.append(tk.Label(self.root, text=ptext, width=40, fg="Red"))
        self.widgets[len(self.widgets)-1].place(relx=0.5, x=-160, y=110)

    # waiting for connection
    def widget_show_life(self):
        self.widgets.append(tk.Label(self.root, text="Life: "+str(self.turns.life), width=20, fg="Red"))
        self.widgets[len(self.widgets)-1].place(x=5, y=5)

    # ip entry
    def widget_ip_input(self):
        self.widgets.append(tk.Entry(self.root, width=20))
        self.widgets[len(self.widgets)-1].insert(0, "127.0.0.1")
        self.widgets[len(self.widgets)-1].place(relx=0.5, x=-80, y=133)

    # connect to host button
    def widget_connect_button(self):
        self.widgets.append(tk.Button(self.root))
        self.widgets[len(self.widgets)-1]["text"] = "Connect"
        self.widgets[len(self.widgets)-1]["width"] = 10
        self.widgets[len(self.widgets)-1]["height"] = 3
        self.widgets[len(self.widgets)-1]["command"] = self.start_turns_player_2
        self.widgets[len(self.widgets)-1].place(relx=0.5, y=156, x=-50)

    # build up a map from buttons. we can give them action and a map work from
    def widget_print_map(self, map="", action=""):
        currenty = 0
        currentx = 0

        for j in range(0, 10):
            currenty = 185 + (j*30)
            for i in range(0, 10):
                currentx = 238 + (i*30)
                if str(map[j][i]).isdigit():
                    if map[j][i] == 0:
                        self.place_map_label("Blue", j, i, currentx, currenty)
                    elif map[j][i] > 0:
                        self.place_map_label("Green", j, i, currentx, currenty)
                else:
                    if map[j][i] == "x":
                        self.place_map_label("Yellow", j, i, currentx, currenty)
                    elif map[j][i] == "h":
                        self.place_map_label("Red", j, i, currentx, currenty)

    def place_map_label(self, color, j, i, currentx, currenty):
        self.widgets.append(tk.Label(self.root))
        self.widgets[len(self.widgets)-1]["text"] = str(j)+""+str(i)
        self.widgets[len(self.widgets)-1]["width"] = 2
        self.widgets[len(self.widgets)-1]["height"] = 1
        self.widgets[len(self.widgets)-1]["bg"] = color
        self.widgets[len(self.widgets)-1].place(y=currenty, x=currentx)

    def widget_horizontal_or_vertical_radio(self):
        self.widgets.append(tk.Radiobutton(self.root, variable=self.horizontal_or_vertical, value=0, command=self.set_orientation_horizontal))
        self.widgets[len(self.widgets)-1]["text"] = "Horizontal"
        self.widgets[len(self.widgets)-1].place(y=155, x=240)

        self.widgets.append(tk.Radiobutton(self.root, variable=self.horizontal_or_vertical, value=1, command=self.set_orientation_vertical))
        self.widgets[len(self.widgets)-1]["text"] = "Vertical"
        self.widgets[len(self.widgets)-1].deselect()
        self.widgets[len(self.widgets)-1].place(y=155, x=460)

    def set_orientation_horizontal(self):
        self.horizontal_or_vertical = "H"

    def set_orientation_vertical(self):
        self.horizontal_or_vertical = "V"

    # Coordinate input
    def widget_coo_input(self):
        self.widgets.append(tk.Entry(self.root, width=20))
        self.widgets[len(self.widgets)-1].place(relx=0.5, x=-80, y=133)

    # set window size and place bg image
    def configure_window(self):
        self.root.minsize(width=800, height=600)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bgimg = tk.PhotoImage(file=self.getAbsPath()+"../bg.gif")
        self.bg = tk.Label(self.root, image=self.bgimg)
        self.bg.img = self.bgimg
        self.bg.place(x=0, y=0, relwidth=1, relheight=1)

    # empty the screen
    def clear_widgets(self):
        for widget in self.widgets:
            widget.place_forget()
        self.widgets = []

    # !!! SYSTEM FUNCTIONS !!!
    # create turns class for player 1
    def start_turns_player_1(self):
        self.host_widgets()
        self.turns = HandleTurns(1, self)
        _thread.start_new_thread(self.turns.start_game, ())

    # create turns class for player 2
    def start_turns_player_2(self):
        ip = self.get_textarea_value()
        self.turns = HandleTurns(2, self, ip)
        _thread.start_new_thread(self.turns.start_game, ())

    # return string
    def get_textarea_value(self):
        for widget in self.widgets:
            if type(widget) == tk.Entry:
                return widget.get()
        return False

    def handle_placeship(self):
        coo = self.get_textarea_value()
        coo = self.horizontal_or_vertical+" "+str(int(coo[0])+1)+" "+str(int(coo[1])+1)
        no_errors = self.turns.map.placeShip(coo, self.turns.all_ships[self.turns.current_ship])
        has_next_ship = self.turns.nextShip()

        if not has_next_ship:
            self.turns.socket.sendData(self.turns.map.serialize(self.turns.map.myMap))

            if self.turns.player == 1:
                self.waiting_for_enemy_to_place_ships_with_map(self.turns.map)
                _thread.start_new_thread(self.turns.get_enemy_map, ())

            else:
                self.start_shooting()

        if no_errors and has_next_ship:
            self.place_ships_widgets(self.turns.map)

        elif not no_errors:
            self.error_on_place_ships_widgets(self.turns.map)
            self.turns.preShip()

    def handle_shoot(self):
        coo = self.get_textarea_value()
        tmpj = int(coo[0])
        tmpi = int(coo[1])

        if type(self.turns.map.enemyMap[tmpj][tmpi]) == str and self.turns.map.enemyMap[tmpj][tmpi] != "0":
            self.turns.map.shotMap[tmpj][tmpi] = "h"
            self.turns.socket.sendData("hit")

        elif type(self.turns.map.enemyMap[tmpj][tmpi]) == str and self.turns.map.enemyMap[tmpj][tmpi] == "0":
            self.turns.map.shotMap[tmpj][tmpi] = "x"
        self.shoot_widgets()

    def start_shooting(self):
        _thread.start_new_thread(self.turns.get_endless_socket, ())
        self.shoot_widgets()

    def on_closing(self):
        self.turns.socket.closeSocket()
        self.root.destroy()

    def getAbsPath(self):
        return os.path.dirname(os.path.abspath(__file__))+"/"
