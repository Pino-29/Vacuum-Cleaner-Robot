from random import randint, choice
MAX_ROOMS = 5


class Environment:
    __rooms = 0
    __currentRoom = -1
    __state = []
    
    def __init__(self):
        print()
        self.__currentRoom = randint(1, self.__rooms)
        # self.__rooms = randint(1, MAX_ROOMS)
        
        # for room in range(0, self.__rooms):
        #     self.__state.append(choice([True, False]))

    def show(self):
        print(self.__rooms)
        print(self.__currentRoom)
        print(self.__state) # ??
        print() * 3

def main():
    print()
    env = Environment()
    # env.show()

if __name__ == "__main__":
    main()
    main()
    main()
        
