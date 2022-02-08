from random import randint, choice  

MAX_ROOMS = 5
CLEAN = True  
DIRTY = False 

class Environment:
    __rooms = 0
    __state = []
    
    def __init__(self):
        self.__rooms = randint(1, MAX_ROOMS)
        
        for room in range(0, self.__rooms):
            self.__state.append(choice([True, False]))
    
    def show(self):
        print("Number of rooms: ", self.__rooms)
        print("State of each room: ", self.__state) # ??
        print("\n\n")
    
    def isClean(self, room): 
        if (room < 1 or self.__rooms < room):
            raise TypeError("Room is out of bounds.")
        return self.__state[room - 1]
    

    def optimalSolution(self, startingRoom):
        # startingRoom = self.__currentRoom
        solutionOne = solutionTwo = 0
        
        # To left and then to right
        currentRoom = indexRoom = startingRoom
        while (indexRoom >= 1):
            if (self.__state[indexRoom - 1] == DIRTY):
                solutionOne += abs(currentRoom - indexRoom) + 1
                currentRoom = indexRoom
            indexRoom -= 1

        indexRoom = startingRoom + 1
        while (indexRoom <= self.__rooms):
            if (self.__state[indexRoom - 1] == DIRTY):
                solutionOne += abs(currentRoom - indexRoom) + 1
                currentRoom = indexRoom
            indexRoom += 1
        
        # To right and then to left
        currentRoom = indexRoom = startingRoom
        while (indexRoom <= self.__rooms):
            if (self.__state[indexRoom - 1] == DIRTY):
                solutionTwo += abs(currentRoom - indexRoom) + 1
                currentRoom = indexRoom
            indexRoom += 1

        indexRoom = startingRoom - 1
        while (indexRoom >= 1):
            if (self.__state[indexRoom - 1] == DIRTY):
                solutionTwo += abs(currentRoom - indexRoom) + 1
                currentRoom = indexRoom
            indexRoom -= 1


        return min(solutionOne, solutionTwo)

    def getRooms(self):
        return self.__rooms
