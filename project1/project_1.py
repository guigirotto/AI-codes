#
# Artificial intelligence - Project 1
# Computer Engeneering - Semester 9
# Genetic Algoritm - Using Roullete or Tornment method
# Date February 09, 2020
#

from project1.view.user_input import get_values_from_user
from project1.model.GeneticAlgoritm import GeneticAlgoritm
import random
from project1.control.functions import format_binary_code

def run_genetic_algoritm():
    #creating genetic algoritm object class
    #inputResult = get_values_from_user()

    #use only to test
    print('---ATENTION: Do not forget to erase the test code input ---- ')
    inputResult = GeneticAlgoritm(8,40, 1, 1, 1, 1, 1, 1)

    if not inputResult:
        print('Ops, something went wrong')
        return

    #generating chromossome list
    chromossomeBinaryList = []

    for item in range(int(inputResult.populationSize)):
        maxValue = 2**inputResult.chromossomeSize
        #print("----" + str(maxValue) + "----")
        randomValue = random.randrange(maxValue)
        binaryCode = bin(randomValue)
        
        chromossomeBinaryList.append(binaryCode)

    inputResult.currentChromossomeList = []

    #converting the chromossome and populate the current list
    for item in chromossomeBinaryList:
        inputResult.currentChromossomeList.append(format_binary_code(item))
    

