#
# Artificial intelligence - Project 1
# Computer Engeneering - Semester 9
# Genetic Algoritm - Using Roullete or Tornment method
# Date February 09, 2020
#

from project1.view.user_input import get_values_from_user
from project1.model.GeneticAlgoritm import GeneticAlgoritm
from project1.model.Chromossome import Chromossome
import random
from project1.control.functions import *

def run_genetic_algoritm():
    #creating genetic algoritm object class
    #inputResult = get_values_from_user()

    #use only to test
    print('---ATENTION: Do not forget to erase the test code input ---- ')
    inputResult = GeneticAlgoritm(8,40, 1, 30, 1, 1, 2, 1)
    inputResult.setTournmentSize(10)

    if not inputResult:
        print('Ops, something went wrong')
        return

    #generating chromossome list
    chromossomeBinaryList = []

    maxValue = 2**inputResult.chromossomeSize
    for item in range(int(inputResult.populationSize)):
        #print("----" + str(maxValue) + "----")
        randomValue = random.randrange(maxValue)
        binaryCode = bin(randomValue)
        
        chromossomeBinaryList.append(binaryCode)

    inputResult.currentChromossomeList = []

    #converting the chromossome and populate the current list
    for item in chromossomeBinaryList:
        newChromossome = Chromossome(format_binary_code(item, inputResult.chromossomeSize))
        binX, binY = newChromossome.geneticCode[:int(len(newChromossome.geneticCode)/2)] , newChromossome.geneticCode[int(len(newChromossome.geneticCode)/2):]
        realX = inputResult.getConvertionFromBinaryToRealX(binX)
        realY = inputResult.getConvertionFromBinaryToRealY(binY)
        #print(newChromossome.geneticCode,binX, binY)
        fitness = calculate_fitness(realX, realY)
        #print(realX, '\t' ,realY, '\t' ,fitness)

        newChromossome.setFitness(fitness)

        inputResult.currentChromossomeList.append(newChromossome)

    #inputResult.printChromossomes()
    bestChromosome = get_best_chromossome(inputResult.currentChromossomeList)
    #inputResult.setBestChromossome(bestChromosome.geneticCode,0,bestChromosome.fitness)
    test = make_crossover(inputResult)
    #print(test)
    #print(len(test))
    print(inputResult.currentChromossomeList[0].geneticCode)
    testMutation = make_mutation(inputResult,inputResult.currentChromossomeList[0])
    print(testMutation.geneticCode)
    print('-----------------------------------------\n')
    print(make_tournment_selection(inputResult))
    






