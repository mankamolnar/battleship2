from abc import ABC, abstractmethod


class TurnsAbstract(ABC):

    @abstractmethod
    def whosTheFirst(self, player):
        pass

    @abstractmethod
    def scrGetIP(self):
        pass

    @abstractmethod
    def handlePlaceShipResponse(self, response):
        pass

    @abstractmethod
    def getIpAndStartSocket(self):
        pass

    @abstractmethod
    def scrPlaceShip(self):
        pass

    @abstractmethod
    def placeShipLoop(self):
        pass

    @abstractmethod
    def nextShip(self, noError, shipLength, firstThreeLongShip):
        pass

    @abstractmethod
    def isFirstThreeLongShip(self, shipLength, firstThreeLongShip):
        pass

    @abstractmethod
    def finishedPlacing(self, shipLength):
        pass

    @abstractmethod
    def scrShootShip(self):
        pass

    @abstractmethod
    def drawPlaceShip(self):
        pass
