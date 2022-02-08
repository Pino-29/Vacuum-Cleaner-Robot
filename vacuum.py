from environment import Environment
from random import randint 


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
        
