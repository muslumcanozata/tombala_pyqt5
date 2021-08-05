import numpy as np
import random

from numpy.core.fromnumeric import size


class Stamp:
    def __init__(self):
        self.__taken = 0
        self.__takenNumbers = [0]
        self.__rows = 3
        self.__columns = 5
        self.__stamp = [[0]*self.__columns]*self.__rows
        self.__tempList = []
        self.__point = 0
        self.__tempRow = 3

    #set and get the point
    def setPoint(self, numb):
        self.__point = numb
    def getPoint(self):
        return self.__point
    #set and get the tempRow
    def setTempRow(self, numb):
        self.__tempRow = numb
    def getTempRow(self):
        return self.__tempRow
    #set and get the stamp
    def getStampValue(self, column, row):
        return self.__stamp[column][row]
    # set and get the picked number
    def setTaken(self, numb):
        self.__taken = numb
    def getTaken(self):
        return self.__taken

    # set and get the row and column numbers
    def setRow(self, numb):
        self.__rows = numb
    def getRow(self):
        return self.__rows
    def setColumn(self, numb):
        self.__columns = numb
    def getColumn(self):
        return self.__column
    # set and get the numbers list    
    def setStamp(self, list):
        self.__stamp = list
    def getStamp(self):
        return self.__stamp
    
    # set and get the temp list
    def setTempList(self,numb):
        self.__tempList.append(numb)
    def getTempList(self):
        return self.__tempList
    
    #set and get all picked numbers
    def setTakenNumbers(self,list):
        self.__takenNumbers = list
    def getTakenNumbers(self):
        return self.__takenNumbers
    
    # generate random and unique numbers for stamp
    def generateRandomNumber(self):
        list = np.random.choice(np.arange(1,91), replace = False, size=(3,5))
        for i in range(3):
            list[i].sort()
        
        #checked the every elements
        self.setStamp(list)
        
    # generate random and unique picked number from bag
    def takeRandom(self):
        while(1):
            self.__taken = random.randint(1,91)
            if self.__taken not in self.__tempList:
                self.__tempList.append(self.__taken)
                return self.__taken

    def checkTakenNumber(self,numb):
        for x in range(self.__rows):
            for y in range(self.__columns):
                if numb == self.__stamp[x][y]:
                    self.__stamp[x][y] = 0
                    
    def checkBingo(self):
        tempRow = [0]*3
        for x in range(self.__rows):
            for y in range(self.__columns):
                if  self.__stamp[x][y] == 0 :
                    tempRow[x] = tempRow[x]+1
        k=0
        for i in range(3):
            if tempRow[i] == 5:
                k=k+1
        if k == 1:
            self.setPoint(10)
        elif k == 2:
            self.setPoint(30)
        elif k == 3:
            self.setPoint(70)
        k=0
