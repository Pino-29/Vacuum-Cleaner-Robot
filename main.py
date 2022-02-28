# Part 3

from environment import Environment
from vacuum import Vacuum
    
def main():
    vacuum = Vacuum() #
    vacuum.show()

    it = 0
    while vacuum.hasCleanedEverything() == False:
        # print("Is everything clear? ", vacuum.hasCleanedEverything())
        vacuum.run()
        vacuum.show()
        it += 1

    print("Total movements: ", vacuum.timeSpent())
    
if __name__ == "__main__":
    main()
    