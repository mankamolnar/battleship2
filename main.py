import unittest
from copy import copy, deepcopy

#class for the map
class Map:

    #conctruct || inits empty map
    def __init__(self):
        self.myMap = []
        for i in range(0,10):
            self.myMap.append([])
            for j in range(0,10):
                self.myMap[i].append([])
                self.myMap[i][j] = 0
        self.enemyMap = deepcopy(self.myMap)
        self.shotMap = deepcopy(self.myMap)

    #!!! PLACESHIP !!!
    #placing down a ship on myMap
    def placeShip(self, coordinate, length):
        if self.testCoordinate(coordinate) and self.testLength(length) and self.shipInRange(coordinate, length) and self.noShipCollide(coordinate, length):
            coordinate = self.cooToList(coordinate)
            if coordinate[0] == "H":
                for i in range(0,length):
                    self.myMap[coordinate[1]][coordinate[2]+i] = length
            if coordinate[0] == "V":
                for i in range(0,length):
                    self.myMap[coordinate[1]+i][coordinate[2]] = length
        else:
            return False
    
    #testing the given coordinate
    def testCoordinate(self, coordinate):
        if isinstance(coordinate, str) and len(coordinate.strip().split(" ")) == 3 and coordinate.strip().split(" ")[1].isdigit() and coordinate.strip().split(" ")[2].isdigit():
            return True
        return False

    #testing the given length
    def testLength(self, length):
        if str(length).strip() != "" and isinstance(length, int):
            return True
        return False
    
    #converting and casting coordinates to list
    def cooToList(self, coordinate):
        coordinate = str(coordinate).strip().split(" ")
        coordinate[1] = int(coordinate[1])-1
        coordinate[2] = int(coordinate[2])-1
        return coordinate

    #Testing the first and last modul of ship that is it in range or not
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

    #!!! DANGER ZONE !!!
    #EMPTY MAP
    def emptyMap(self, whichMap):
        for i in range(0,10):
            for j in range(0,10):
                if whichMap == "my":
                    self.myMap[i][j] = 0
                elif whichMap == "enemy":
                    self.enemyMap[i][j] = 0

#class for map testing
class MapTest(unittest.TestCase):
    
    map = Map()
    placeship_horizontal_test_matrix = [[5, 5, 5, 5, 5, 0, 0, 0, 0, 0], \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    placeship_horizontal_test_matrix_2 = [[0, 0, 0, 0, 0, 5, 5, 5, 5, 5], \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    placeship_horizontal_test_matrix_3 = [[5, 5, 5, 5, 5, 4, 4, 4, 4, 0], \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    placeship_vertical_test_matrix = [[5, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    placeship_vertical_test_matrix_2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 5],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 5],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 5],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 5],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 5]]
    placeship_vertical_test_matrix_3 = [[5, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [4, 4, 4, 4, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    #testing the construct
    def test_init(self):
        self.assertEqual(len(self.map.myMap), 10)
        self.assertEqual(len(self.map.myMap[0]), 10)
    
    #testing the placeship method. checks the the place where it has put the ship, orientation, and that you cannot place it out of range
    def test_placeShip(self):
        #horizontal place test
        self.map.placeShip("H 1 1", 5)
        self.assertCountEqual(self.map.myMap, self.placeship_horizontal_test_matrix)
        self.map.emptyMap("my")

        #vertical place test
        self.map.placeShip("V 1 1", 5)
        self.assertCountEqual(self.map.myMap, self.placeship_vertical_test_matrix)
        self.map.emptyMap("my")

        #horizontal out of range test | 1. should be placed 2. should return false
        self.map.placeShip("H 1 6", 5)
        self.assertCountEqual(self.map.myMap, self.placeship_horizontal_test_matrix_2)
        self.map.emptyMap("my")
        self.assertFalse(self.map.placeShip("H 1 7", 5))

        #vertical out of range test | 1. should be placed 2. should return false
        self.map.placeShip("V 6 10", 5)
        self.assertCountEqual(self.map.myMap, self.placeship_vertical_test_matrix_2)
        self.map.emptyMap("my")
        self.assertFalse(self.map.placeShip("V 7 10", 5))
        self.assertFalse(self.map.placeShip("H 0 1", 5))
        self.assertFalse(self.map.placeShip("H 1 0", 5))

        #horizontal ship collide test | 1. should be placed 2. should return false
        self.map.placeShip("H 1 1", 5)
        self.map.placeShip("H 1 6", 4)
        self.assertCountEqual(self.map.myMap, self.placeship_horizontal_test_matrix_3)
        self.map.emptyMap("my")
        self.map.placeShip("H 1 5", 4)
        self.assertFalse(self.map.placeShip("H 1 1", 5))
        self.map.emptyMap("my")

        #testing illegal arguments
        self.assertFalse(self.map.placeShip(5, 5))
        self.assertFalse(self.map.placeShip("", 5))
        self.assertFalse(self.map.placeShip("ha1", 5))
        self.assertFalse(self.map.placeShip("H 1", 5))
        self.assertFalse(self.map.placeShip("H 1 1", 0))
        self.assertFalse(self.map.placeShip("H 1 1", "a5"))
    
    #testing the shoting method for out of range, double shot at the same place
    def test_shot(self):
        self.assertFalse(self.map.shot("0 1"))
        self.assertFalse(self.map.shot("1 0"))
        self.assertFalse(self.map.shot("1"))
        self.assertFalse(self.map.shot("1 1 1"))
        self.assertFalse(self.map.shot(1))
        self.assertFalse(self.map.shot('éakjfafs'))
        self.assertFalse(self.map.shot(''))
        self.map.shot("1 1")
        self.assertEqual(self.map.shot("1 1"), "[shotHere]")
        
        self.map.enemyMap = deepcopy(self.placeship_vertical_test_matrix_3)
        self.map.shot("2 1")
        self.assertEqual(self.map.shot("2 1"), "[shotHere]")


#map = Map()
unittest.main()