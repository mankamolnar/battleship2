# imports
from copy import copy, deepcopy
from classes.model.MapAbstract import MapAbstract


class Map(MapAbstract):

    # conctruct || inits empty map
    def __init__(self):
        self.myMap = []
        for i in range(0,10):
            self.myMap.append([])
            for j in range(0,10):
                self.myMap[i].append([])
                self.myMap[i][j] = 0
        self.enemyMap = deepcopy(self.myMap)
        self.shotMap = deepcopy(self.myMap)

    # !!! PLACESHIP !!!
    # placing down a ship on myMap
    def placeShip(self, coordinate, length):
        if self.testCoordinate(coordinate) and self.testLength(length) and self.shipInRange(coordinate, length) and self.noShipCollide(coordinate, length):
            coordinate = self.cooToList(coordinate)
            if coordinate[0] == "H":
                for i in range(0,length):
                    self.myMap[coordinate[1]][coordinate[2]+i] = length
            if coordinate[0] == "V":
                for i in range(0,length):
                    self.myMap[coordinate[1]+i][coordinate[2]] = length
            return True
        else:
            return False

    # testing the given coordinate
    def testCoordinate(self, coordinate):
        if isinstance(coordinate, str) and len(coordinate.strip().split(" ")) == 3 and coordinate.strip().split(" ")[1].isdigit() and coordinate.strip().split(" ")[2].isdigit():
            return True
        return False

    # testing the given length
    def testLength(self, length):
        if str(length).strip() != "" and isinstance(length, int):
            return True
        return False
    
    # converting and casting coordinates to list
    def cooToList(self, coordinate):
        coordinate = str(coordinate).strip().split(" ")
        coordinate[1] = int(coordinate[1])-1
        coordinate[2] = int(coordinate[2])-1
        return coordinate

    # Testing the first and last modul of ship that is it in range or not
    def shipInRange(self, coordinate, length):
        coordinate = self.cooToList(coordinate)
        length -= 1
        if coordinate[0] == "H":
            if coordinate[1] >= 0 and coordinate[1] < 10 and coordinate[2] >= 0 and coordinate[2] < 10 and coordinate[2] + length >= 0 and coordinate[2] + length < 10:
                return True
        elif coordinate[0] == "V":
            if coordinate[1] >= 0 and coordinate[1] < 10 and coordinate[2] >= 0 and coordinate[2] < 10 and coordinate[1] + length >= 0 and coordinate[1] + length < 10:
                return True
        return False
    
    #Testing for ship collide
    def noShipCollide(self, coordinate, length):
        coordinate = self.cooToList(coordinate)
        length -= 1
        if coordinate[0] == "H":
            for i in range(0,length):
                if self.myMap[coordinate[1]][coordinate[2]+i] > 0:
                    return False
        if coordinate[1] == "V":
            for i in range(0,length):
                if self.myMap[coordinate[1]+i][coordinate[2]] > 0:
                    return False
        return True
    
    #!!! SHOT !!!
    #shooting to someone
    def shot(self, coordinate):
        if self.testShotCoordinate(coordinate) and self.testShotCooInRange(coordinate):
            if self.haventShotHere(coordinate):
                coordinate = self.shotCooToList(coordinate)
                if self.enemyMap[coordinate[0]][coordinate[1]] == 0: 
                    self.shotMap[coordinate[0]][coordinate[1]] = "x"
                else:
                    self.shotMap[coordinate[0]][coordinate[1]] = self.enemyMap[coordinate[0]][coordinate[1]]
            else:
                return "[shotHere]"
        else:
            return False
    
    #testing down the coordinates format
    def testShotCoordinate(self, coordinate):
        if isinstance(coordinate, str) and len(coordinate.strip().split(" ")) == 2 and coordinate.strip().split(" ")[0].isdigit() and coordinate.strip().split(" ")[1].isdigit():
            return True
        return False

    #testing that the coordinates are in range
    def testShotCooInRange(self, coordinate):
        coordinate = self.shotCooToList(coordinate)
        if coordinate[0] >= 0 and coordinate[0] < 10 and coordinate[1] >= 0 and coordinate[1] < 10:
            return True
        return False

    #checking that you've already shot the coordinates
    def haventShotHere(self, coordinate):
        coordinate = self.shotCooToList(coordinate)
        if str(self.shotMap[coordinate[0]][coordinate[1]]) == "0":
            return True
        else:
            return False
    
    #shot coordinate to list
    def shotCooToList(self, coordinate):
        coordinate = coordinate.strip().split(" ")
        coordinate[0] = int(coordinate[0])-1
        coordinate[1] = int(coordinate[1])-1
        return coordinate

    #!!! DRAW MAP !!!
    #draw
    def draw(self, map):
        print("   1 2 3 4 5 6 7 8 9 10")
        for i in range(0,len(map)):
            linestr = str(i+1)+self.defineSpaces(i)
            for j in range(0, len(map[i])):
                linestr += str(map[i][j])+" "
            print(linestr)
    
    #define how many spaces do you need for the draw line
    def defineSpaces(self, i):
        if len(str(i+1)) == 1:
            return "  "
        else:
            return " "
    
    #serialize map
    def serialize(self, map):
        string = ""
        for i in range(0, len(map)):
            for j in range(0, len(map[i])):
                string += str(map[i][j])
        return string

    #serialized map to list
    def serToMap(self, serialized):
        counter = 0
        tmpMap = []
        for i in range(0,10):
            tmpMap.append([])
            for j in range(0,10):
                tmpMap[i].append([])
                tmpMap[i][j] = serialized[counter]
                counter += 1
        return tmpMap

    #!!! DANGER ZONE !!!
    #EMPTY MAP
    def emptyMap(self, whichMap):
        for i in range(0,10):
            for j in range(0,10):
                if whichMap == "my":
                    self.myMap[i][j] = 0
                elif whichMap == "enemy":
                    self.enemyMap[i][j] = 0