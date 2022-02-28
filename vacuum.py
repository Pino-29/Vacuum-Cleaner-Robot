from environment import Environment
from random import randint 

LEFT = False
RIGHT = True

class Vacuum:
    def __init__(self):
        self.environment = Environment()
        self.__operationsDone = 0
        self.__flag = False
        self.__direction = LEFT 
        self.__optimalSolution = 0

        self.__currentRoom = self.__startingRoom = randint(1, self.environment.getRooms())

        self.__visited = []
        for i in range(0, self.environment.getRooms()):
            self.__visited.append(False)
        self.mark(self.getCurrentRoom())
        
        if self.getCurrentRoom() <= self.environment.getRooms() // 2:
            self.__direction = LEFT
        else:
            self.__direction = RIGHT
        self.__optimalSolution = self.environment.optimalSolution(self.getCurrentRoom())


    def mark(self, room):
        if self.environment.insideRange(room) == False:
            raise TypeError("Room is out of bounds.")
        self.__visited[room - 1] = True

    def performance(self):
        if self.timeSpent() == 0:
            return 100.
        return (float)(self.__optimalSolution / self.timeSpent()) * 100

    def show(self):
        print("Current room: ", self.__currentRoom)
        print("Direction: ", end = "")
        if (self.__direction == LEFT):
            print("left")
        else:
            print("right")
        print(self.__visited)
        self.environment.show()

    def getOptimalSolution(self):
        return self.__optimalSolution

    def getCurrentRoom(self):
        return self.__currentRoom

    def setCurrentRoom(self, currentRoom):
        self.__currentRoom = currentRoom

    def currentRoomDirty(self):
        return self.environment.isClean(self.getCurrentRoom()) == False   
    
    def hasCleanedEverything(self):
        return self.__visited.count(False) == 0 and self.environment.completelyClean()


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
        if self.__flag == False:
            if (self.__direction == RIGHT and self.getCurrentRoom() == self.environment.getRooms()) \
             or (self.__direction == LEFT and self.getCurrentRoom() == 1):
                # change your direction
                if self.__direction == LEFT:
                    self.__direction = RIGHT
                else:
                    self.__direction = LEFT
                self.__flag = True


    def run(self):
        # print("run... ", self.currentRoomDirty())
        if self.currentRoomDirty() == True:
            self.suck()
        else:
            # print("Optimal Movement: ", self.__optimalMovement())
            self.__optimalMovement()
            if self.__direction == RIGHT:
                self.moveRight()
            else:
                self.moveLeft()
            self.mark(self.getCurrentRoom()) 
    

    def timeSpent(self):
        return self.__operationsDone

    

