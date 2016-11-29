import os
from classes.MapClass import Map
from classes.SocketClass import Socket, ServerSocket, ClientSocket
import _thread


class HandleTurns:

    def __init__(self, player, gui, ip="127.0.0.1"):
        self.gui = gui
        self.player = int(player)
        self.map = Map()
        self.current_ship = 0
        self.all_ships = [2, 3, 3, 4, 5]

        if self.player == 1:
            self.socket = ServerSocket()
        else:
            self.socket = ClientSocket(ip)
        
        self.checkConnection(self.socket.startSocket())

    # defining who's turn is the first (player1 = first, player2 = second)
    def whosTheFirst(self, player):
        if player == 1:
            return True
        elif player == 2:
            return False

    # handle the successful or unsuccessful connection
    def checkConnection(self, connected):
        if self.player == 1:
            if connected:
                self.gui.place_ships_widgets(self.map)

        elif self.player == 2:
            if connected:
                self.gui.waiting_for_enemy_to_place_ships()
                self.start_get_map_thread()
            else:
                self.gui.client_on_error_widgets()

    def start_get_map_thread(self):
        _thread.start_new_thread(self.get_enemy_map, ())

    def get_enemy_map(self):
        serializedMap = self.socket.receiveData()
        self.map.enemyMap = self.map.serToMap(serializedMap)
        print(self.map.enemyMap)

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