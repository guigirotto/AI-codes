#
# Artificial intelligence - Project 1
# Computer Engeneering - Semester 9
# Genetic Algoritm - Using Roullete or Tornment method
# Date February 09, 2020
#
from project1.view.result_display import show_chart
from project1.view.result_display import show_chart2
from project1.view.user_input import get_values_from_user
from project1.model.GeneticAlgoritm import GeneticAlgoritm
from project1.model.Chromossome import Chromossome
import random
from project1.control.functions import *
import matplotlib.animation as animation

def run_genetic_algoritm():
    # creating genetic algoritm object class
    #inputResult = get_values_from_user()

    # Use only to test
    print('---ATENTION: Do not forget to erase the test code input ---- ')
    #To remember
    #    def __init__(chromossomeSize, populationSize, crossingProbability,
     #mutationProbability,methodOfSelection, elitismSize,
     # quantityOfCrossing, quantityOfGeneration):
    inputResult: GeneticAlgoritm = GeneticAlgoritm(20, 20, 30, 10, 1, 0, 1, 50)
    inputResult.setTournmentSize(4)

    if not inputResult:
        print('Ops, something went wrong')
        return

    #generating chromossome list
    chromossomeBinaryList = []
    bestChromossomeList = []

    maxValue = 2**inputResult.chromossomeSize
    for item in range(int(inputResult.populationSize)):
        randomValue = random.randrange(maxValue)
        binaryCode = bin(randomValue)
        
        chromossomeBinaryList.append(binaryCode)

    inputResult.currentChromossomeList = []
    actualGeneration = 0

    # converting the chromossome and populate the current list
    for item in chromossomeBinaryList:
        newChromossome = Chromossome(format_binary_code(item, inputResult.chromossomeSize),actualGeneration)
        binX, binY = newChromossome.geneticCode[:int(len(newChromossome.geneticCode)/2)] , newChromossome.geneticCode[int(len(newChromossome.geneticCode)/2):]
        realX = inputResult.getConvertionFromBinaryToRealX(binX)
        realY = inputResult.getConvertionFromBinaryToRealY(binY)
        fitness = calculate_fitness(realX, realY)
        newChromossome.setFitness(fitness)
        inputResult.currentChromossomeList.append(newChromossome)

    sumFitness = calculate_fitness_sum(inputResult)
    sumProb = 0

    for index,item in enumerate(inputResult.currentChromossomeList):
        if index == 0:
            probability  = calculate_roulette_probability(item.fitness,sumFitness)
            item.setProbability(probability)
            sumProb += probability
        else:
            probability  = calculate_roulette_probability(item.fitness,sumFitness)
            sumProb += probability
            item.setProbability(sumProb)

    bestChromosome = get_best_chromossome(inputResult.currentChromossomeList)
    bestChromossomeList.append(bestChromosome)
    actualGeneration += 1
    while actualGeneration < inputResult.quantityOfGeneration:
        newChromossomeList = []
       
        #crossover
        if inputResult.methodOfSelection == 1:
            crossoverChromossomesGeneticCodes = make_crossover(inputResult,generation = actualGeneration)
            #Need to create chromossome and add on the new list
            for newChromossome in crossoverChromossomesGeneticCodes:

                binX, binY = newChromossome.geneticCode[:int(len(newChromossome.geneticCode)/2)] , newChromossome.geneticCode[int(len(newChromossome.geneticCode)/2):]
                realX = inputResult.getConvertionFromBinaryToRealX(binX)
                realY = inputResult.getConvertionFromBinaryToRealY(binY)
                fitness = calculate_fitness(realX, realY)

                newChromossome.setFitness(fitness)
                newChromossomeList.append(newChromossome)


            inputResult.currentChromossomeList = newChromossomeList

        elif inputResult.methodOfSelection == 2:
            #crossover tournment
            crossoverChromossomesGeneticCodes = run_tournment_selection(inputResult, generation=actualGeneration)
            for item in crossoverChromossomesGeneticCodes:

                binX, binY = item.geneticCode[:int(len(item.geneticCode)/2)] , item.geneticCode[int(len(item.geneticCode)/2):]
                realX = inputResult.getConvertionFromBinaryToRealX(binX)
                realY = inputResult.getConvertionFromBinaryToRealY(binY)
                fitness = calculate_fitness(realX, realY)
                item.setFitness(fitness)

            inputResult.currentChromossomeList = crossoverChromossomesGeneticCodes
        # list complete

        #Mutations
        for index,item in enumerate(inputResult.currentChromossomeList):
            #Keep the elitism without mutations
            if not (index < inputResult.elitismSize):
                item = make_mutation(inputResult,item)
        

        #Calculating new fitness after mutations
        for item in inputResult.currentChromossomeList:

            binX, binY = item.geneticCode[:int(len(item.geneticCode)/2)] , item.geneticCode[int(len(item.geneticCode)/2):]
            realX = inputResult.getConvertionFromBinaryToRealX(binX)
            realY = inputResult.getConvertionFromBinaryToRealY(binY)
            fitness = calculate_fitness(realX, realY)

            item.setFitness(fitness)    


        #Calculating chromossome probability for the using on the next crossover if its needed
        sumFitness = calculate_fitness_sum(inputResult)
        sumProb = 0 
        for index,item in enumerate(inputResult.currentChromossomeList):
            if index == 0:
                probability  = calculate_roulette_probability(item.fitness, sumFitness)
                item.setProbability(probability)
                sumProb += probability
            else:
                probability  = calculate_roulette_probability(item.fitness, sumFitness)
                sumProb += probability
                item.setProbability(sumProb)
                
        #Get BestChromossome for each generation        
        bestChromosomeGeneration = get_best_chromossome(inputResult.currentChromossomeList)
        
        bestChromosome = bestChromosomeGeneration
        bestChromossomeList.append(bestChromosome)
        
        actualGeneration += 1

    #end while
    print('\n\n\n----------- Last Population-----------------')
    print(inputResult.printChromossomes())
    print('\n\n\n ------------RESULT---------------- \n')
    for bestChromosome in bestChromossomeList:
        print(
                "CURRENT BEST CHRMOSSOME: " + bestChromosome.geneticCode + 
                "\tGeneration: " + str(bestChromosome.generation) +
                "\tFitness: " + str(bestChromosome.fitness)
        )

    show_chart(bestChromossomeList,inputResult)
    show_chart2(bestChromossomeList,inputResult.quantityOfGeneration)






