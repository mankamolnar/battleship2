import os
from classes.MapClass import Map
from classes.SocketClass import Socket, ServerSocket, ClientSocket
import _thread


class HandleTurns:
    all_ships = [2, 3, 3, 4, 5]
    current_ship = 0

    def __init__(self, player, gui, ip="127.0.0.1"):
        self.gui = gui
        self.player = int(player)
        self.map = Map()
        self.life = 17

        if self.player == 1:
            self.socket = ServerSocket()
        else:
            self.socket = ClientSocket(ip)

    # defining who's turn is the first (player1 = first, player2 = second)
    def whosTheFirst(self, player):
        if player == 1:
            return True
        elif player == 2:
            return False

    # handle the successful or unsuccessful connection
    def start_game(self):
        self.socket.startSocket()
        if self.player == 1:
            if self.socket.started:
                self.gui.place_ships_widgets(self.map)

        elif self.player == 2:
            if self.socket.started:
                self.gui.waiting_for_enemy_to_place_ships()
                self.get_enemy_map()
                self.gui.place_ships_widgets(self.map)

            else:
                self.gui.client_on_error_widgets()

    # get enemy's map through socket
    def get_enemy_map(self):
        serializedMap = self.socket.receiveData()
        self.map.enemyMap = self.map.serToMap(serializedMap)

        if self.player == 1:
            self.gui.start_shooting()

        return True

    # if the response is [readyToPlay] returns True otherwise False
    def handlePlaceShipResponse(self, response):
        if response != "[error]":
            self.map.enemyMap = self.map.serToMap(response)
        else:
            return False

    # which one is the next ship. Returns the length of the next ship
    def nextShip(self):
        self.current_ship += 1
        if len(self.all_ships) > self.current_ship:
            return True
        else:
            return False

    # returns false if it doesnt have previous ship
    def preShip(self):
        self.current_ship -= 1
        if len(self.all_ships) > self.current_ship:
            return True
        else:
            return False

    # !!! SCREEN 3 - shooting part
    def scrShootShip(self):
        if self.myTurn:
            print("Herecomestheshootpart")
        else:
            print("Waiting for the other player to place his ships...")
            response = self.socket.receiveData()

    # drawing for placeships
    def drawPlaceShip(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Player "+str(self.player)+"\n")
        self.map.draw(self.map.myMap)

    # endless socket from shoot part
    def get_endless_socket(self):
        while True:
            answer = self.socket.receiveData()
            if answer == "hit":
                self.life -= 1

                if self.life == 0:
                    #self.
                    pass
                else:
                    self.gui.widgets[len(self.gui.widgets)-1].place_forget()
                    del self.gui.widgets[len(self.gui.widgets)-1]
                    self.gui.widget_show_life()
