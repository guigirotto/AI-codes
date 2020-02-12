#
# Artificial intelligence - Project 1
# Computer Engeneering - Semester 9
# Genetic Algoritm - Using Roullete or Tornment method
# Date February 09, 2020
#
from project_1.control.functions import checkIfUserTypeOnlyDigits


def getValuesFromUser():
    chromossomeSize = input('Inform a chromossome size: ')
    populationSize = input('Inform a population size: ')
    crossingProbability = input('Inform a crossing possibility: ')
    mutationProbability = input('Inform a mutation probability: ')
    quantityOfGeneration = input('Inform the quantity of generations: ')
    methodOfSelection = (input('Inform a selection method to the algoritm \n 1 - Roullete \n 2 - Tournment \n'))
    if not (methodOfSelection.isdigit() and (methodOfSelection == '1' or methodOfSelection == '2')):
        print('Invalid option !')
        return False
    if methodOfSelection == '2':
        tournmentSize = input('Inform the tournment size: ')
    elitismSize = input('Inform the elitism size: ')
    quantityOfCrossing = input('Inform the quantity of crossing: ')
    return checkIfUserTypeOnlyDigits(chromossomeSize, populationSize, crossingProbability,
                                     mutationProbability, methodOfSelection, elitismSize,
                                     quantityOfCrossing, quantityOfGeneration)


def runGeneticAlgoritm():
    inputResult = getValuesFromUser()
    if not inputResult:
        print('Ops, something went wrong')
    else:
        print('Success !')
    return


runGeneticAlgoritm()


