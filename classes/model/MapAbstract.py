# imports
from abc import ABC, abstractmethod


class MapAbstract(ABC):

    @abstractmethod
    def __init__(self):
        pass

    # !!! PLACESHIP !!!
    @abstractmethod
    def placeShip(self, coordinate, length):
        pass

    @abstractmethod
    def testCoordinate(self, coordinate):
        pass

    @abstractmethod
    def testLength(self, length):
        pass

    @abstractmethod
    def cooToList(self, coordinate):
        pass

    @abstractmethod
    def shipInRange(self, coordinate, length):
        pass

    @abstractmethod
    def noShipCollide(self, coordinate, length):
        pass

    # !!! SHOT !!!
    @abstractmethod
    def shot(self, coordinate):
        pass

    @abstractmethod
    def testShotCoordinate(self, coordinate):
        pass

    @abstractmethod
    def testShotCooInRange(self, coordinate):
        pass

    @abstractmethod
    def haventShotHere(self, coordinate):
        pass

    @abstractmethod
    def shotCooToList(self, coordinate):
        pass

    # !!! DRAW MAP !!!
    @abstractmethod
    def draw(self, map):
        pass

    @abstractmethod
    def defineSpaces(self, i):
        pass

    @abstractmethod
    def serialize(self, map):
        pass

    @abstractmethod
    def serToMap(self, serialized):
        pass

    # !!! DANGER ZONE !!!
    @abstractmethod
    def emptyMap(self, whichMap):
        pass
