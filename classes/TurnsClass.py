import os
from classes.MapClass import Map
from classes.SocketClass import Socket, ServerSocket, ClientSocket
# from model.TurnsAbstract import TurnsAbstract


class HandleTurns:

    # !!! CONSTRUCT !!!
    def __init__(self, player, gui, ip="127.0.1.1"):
        self.gui = gui
        self.player = int(player)
        self.map = Map()
        self.myStage = "[placeShips]"
        self.enemyStage = "[placeShips]"
        self.myTurn = self.whosTheFirst(self.player)

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
        if self.player == 2:
            if connected:
                print("Connected")
            else:
                self.gui.client_on_error_widgets()

    # !!! SCREEN 1 - GET IP !!!
    def scrGetIP(self):
        self.getIpAndStartSocket()
        if self.myTurn:
            self.scrPlaceShip()

        elif not self.myTurn:
            print("Waiting for the other player to place his ships...")
            self.myTurn = self.handlePlaceShipResponse(self.socket.receiveData())
            self.scrGetIP()

    # if the response is [readyToPlay] returns True otherwise False
    def handlePlaceShipResponse(self, response):
        if response != "[error]":
            self.map.enemyMap = self.map.serToMap(response)
        else:
            return False

    # asks for the host's ip and starts the socket
    def getIpAndStartSocket(self):
        if not self.socket.started:
            self.socket.HOST = "127.0.1.1"  # input("Please give me the host's IP!")
            self.socket.startSocket()
            self.socket.started = True

    # !!! SCREEN 2 - Place ships !!!
    def scrPlaceShip(self):
        self.placeShipLoop()
        self.socket.sendData(self.map.serialize(self.map.myMap))
        self.myTurn = False
        self.scrShootShip()

    # placeship loop
    def placeShipLoop(self):
        readyToGo = False
        firstThreeLongShip = True
        shipLength = 2

        while readyToGo == False:
            self.drawPlaceShip()
            coordinates = input("Please give the coordinates for a "+str(shipLength)+" long ship!")
            noError = self.map.placeShip(coordinates, shipLength)
            nextShip = self.nextShip(noError, shipLength, firstThreeLongShip)
            firstThreeLongShip = self.isFirstThreeLongShip(shipLength, firstThreeLongShip)
            shipLength = nextShip
            readyToGo = self.finishedPlacing(shipLength)

    # which one is the next ship. Returns the length of the next ship
    def nextShip(self, noError, shipLength, firstThreeLongShip):
        if noError:
            if shipLength == 3 and firstThreeLongShip == True:
                shipLength -= 1
            shipLength += 1
        else:
            print("ERROR! Invalid format or you're trying to place at a wrong place!")
        return shipLength

    # changes the firstThreeLongShip's value when we reach the first three long ship. Returns False
    def isFirstThreeLongShip(self, shipLength, firstThreeLongShip):
        if shipLength == 3 and firstThreeLongShip:
            return False
        else:
            return True

    # checks that we have finished already placing ships. Returns True if we are ready
    def finishedPlacing(self, shipLength):
        if shipLength == 6:
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