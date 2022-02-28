# Agente Reactivo simple, part 2

from environment import Environment
from vacuum import Vacuum
    
def main():
    print("*" * 50) 
    vacuum = Vacuum() #
    vacuum.show()
    
    it = 0
    while vacuum.hasCleanedEverything() == False:
        # print("Is everything clear? ", vacuum.hasCleanedEverything())
        vacuum.run()
        vacuum.show()
        it += 1

    print("Minimum movements: ", vacuum.getOptimalSolution())
    print("Total movements: ", vacuum.timeSpent())
    print(f"Performance: {vacuum.performance()}%")
    
    print()
    return vacuum.performance()

    
if __name__ == "__main__":
    sum = 0.
    iterations = 4
    for i in range(0, iterations):
        sum += main()
    print(f"Average: {sum / iterations}%")
    