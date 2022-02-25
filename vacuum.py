from environment import Environment
from random import randint 

LEFT = False
RIGHT = True

class Vacuum:
    __currentRoom = 0
    __startingRoom = 0
    __operationsDone = 0
    environment = Environment()

    def __init__(self):
        self.__currentRoom = self.__startingRoom = randint(1, self.environment.getRooms())

    def performance(self):
        return (float)(self.__operationsDone / self.environment.optimalSolution(self.__startingRoom))

    def show(self):
        print("Current room: ", self.__currentRoom)
        self.environment.show()

    def getCurrentRoom(self):
        return self.__currentRoom

    def setCurrentRoom(self, currentRoom):
        self.__currentRoom = currentRoom

    def currentRoomDirty(self):
        return self.environment.isClean(self.getCurrentRoom()) == False   
    
    def hasCleanedEverything(self):
        return self.environment.completelyClean()



    def __costOfMovement(self):
        return 1
    
    def __costOfSucking(self):
        return 1



    def getEnvironment(self):
        return self.environment
    
    def setEnvironment(self, environment):
        self.environment = environment


    def moveLeft(self):
        self.__operationsDone += self.__costOfMovement()
        if self.getCurrentRoom() > 1:
            self.setCurrentRoom(self.getCurrentRoom() - 1)
    
    def moveRight(self):
        self.__operationsDone += self.__costOfMovement()
        if self.getCurrentRoom() < self.getEnvironment().getRooms():
            self.setCurrentRoom(self.getCurrentRoom() + 1)
    
    def suck(self):
        self.__operationsDone += self.__costOfSucking()
        self.environment.clean(self.getCurrentRoom())
    

    def __optimalMovement(self): # Identify the best movement
        # hello world :D
        solutionOne = solutionTwo = 0
        
        # To left and then to right
        currentRoom = indexRoom = self.getCurrentRoom()
        while (indexRoom >= 1):
            if self.environment.isClean(indexRoom) == False:
                solutionOne += (abs(currentRoom - indexRoom) * self.__costOfMovement() + self.__costOfSucking())
                currentRoom = indexRoom
            indexRoom -= 1

        indexRoom = self.getCurrentRoom() + 1
        while (indexRoom <= self.environment.getRooms()):
            if self.environment.isClean(indexRoom) == False:
                solutionOne += (abs(currentRoom - indexRoom) * self.__costOfMovement() + self.__costOfSucking())
                currentRoom = indexRoom
            indexRoom += 1
        
        # To right and then to left
        currentRoom = indexRoom = self.getCurrentRoom()
        while (indexRoom <= self.environment.getRooms()):
            if self.environment.isClean(indexRoom) == False:
                solutionTwo += (abs(currentRoom - indexRoom) * self.__costOfMovement() + self.__costOfSucking())
                currentRoom = indexRoom
            indexRoom += 1

        indexRoom = self.getCurrentRoom() - 1
        while (indexRoom >= 1):
            if self.environment.isClean(indexRoom) == False:
                solutionTwo += (abs(currentRoom - indexRoom) * self.__costOfMovement() + self.__costOfSucking())
                currentRoom = indexRoom
            indexRoom -= 1

        if solutionOne < solutionTwo:
            for index in range(1, self.getCurrentRoom() + 1):
                if self.environment.isClean(index) == False:
                    return LEFT 
            return RIGHT
        else:
            for index in range(self.getCurrentRoom(), self.environment.getRooms() + 1):
                if self.environment.isClean(index) == False:
                    return RIGHT 
            return LEFT


    def run(self):
        # print("run... ", self.currentRoomDirty())
        if self.currentRoomDirty() == True:
            self.suck()
        else:
            # print("Optimal Movement: ", self.__optimalMovement())
            if self.__optimalMovement() == RIGHT:
                self.moveRight()
            else:
                self.moveLeft()
    

    def timeSpent(self):
        return self.__operationsDone

    

