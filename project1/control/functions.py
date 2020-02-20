
from project1.model.Chromossome import Chromossome

def check_if_user_type_only_digits(chromossomeSize, populationSize, crossingProbability, mutationProbability,
                              methodOfSelection, elitismSize, quantityOfCrossing, quantityOfGeneration):
    if not chromossomeSize.isdigit(): return False
    if not populationSize.isdigit(): return False
    if not crossingProbability.isdigit(): return False
    if not mutationProbability.isdigit(): return False
    if not methodOfSelection.isdigit(): return False
    if not elitismSize.isdigit(): return False
    if not quantityOfCrossing.isdigit(): return False
    if not quantityOfGeneration.isdigit(): return False
    return True

def format_binary_code(binaryCode, chromossomeSize):
    #getting only the binari part of 0b0101010
    binaryString = str(binaryCode).split("b")[1]
    for i in range(chromossomeSize - len(binaryString)):
        binaryString = "0" + binaryString
    return binaryString

def calculate_fitness(value_x, value_y):
    import math
    result = 21.5 + value_x*math.sin(4*math.pi*value_x) + value_y*math.sin(20*math.pi*value_y)
    return result
    
def calculate_roulette_probability(fitness_value, fitness_summation):
    probability = fitness_value/fitness_summation
    return probability

def calculate_fitness_sum(genetic_algorithm):
    sumFitness = 0
    for item in genetic_algorithm.currentChromossomeList:
        sumFitness += item.fitness
    return sumFitness



def select_chromossome_for_crossover(genetic_algorithm):
    import random
    selectedProb = random.uniform(0,1)
  
    
    for index,item in enumerate(genetic_algorithm.currentChromossomeList):
        if index == 0:
            if 0 <= selectedProb < item.probability:
                selectedChromossome = item
        elif item == genetic_algorithm.currentChromossomeList[-1]:
            if genetic_algorithm.currentChromossomeList[index - 1].probability <=  selectedProb <= 1:
                selectedChromossome = item
        else:
            if genetic_algorithm.currentChromossomeList[index - 1].probability <=  selectedProb < item.probability:
                selectedChromossome = item

   
    return selectedChromossome

def keep_chromossomes_elitism(genetic_algorithm):
    chromossomeList = genetic_algorithm.currentChromossomeList.copy()
    chromossomesToStillList = []
    while len(chromossomesToStillList) < genetic_algorithm.elitismSize:
        bestChromossome = get_best_chromossome(chromossomeList)
        chromossomeList.remove(bestChromossome)
        chromossomesToStillList.append(bestChromossome.geneticCode)

    return chromossomesToStillList    



def make_crossover(genetic_algorithm):
    import random
    canAdd = True
  
    if genetic_algorithm.elitismSize > 0:
        newGeneticCodeList = keep_chromossomes_elitism(genetic_algorithm)
    else:
        newGeneticCodeList=[]

   
    if genetic_algorithm.quantityOfCrossing == 1:
        while len(newGeneticCodeList) < genetic_algorithm.populationSize:
            canAdd = True
            probability = random.randint(1,100)

            firstDad = select_chromossome_for_crossover(genetic_algorithm)
            secondDad = select_chromossome_for_crossover(genetic_algorithm)
            #Testing if it is the same dad
            while firstDad == secondDad:
                secondDad = select_chromossome_for_crossover(genetic_algorithm)
            

            #Test if the chromossomes can make a crossover. If not, keep the selected dads  for the next generation.
            if probability > genetic_algorithm.crossingProbability:
                newGeneticCodeList.append(firstDad.geneticCode)
                newGeneticCodeList.append(secondDad.geneticCode)
                

            
            else:
                #It can't be 0. When we get 0, no separation occurs 
                  
                indexSeparation = random.randint(1,(genetic_algorithm.chromossomeSize -1))
                
                firstGeneticCode = firstDad.geneticCode[:indexSeparation] + secondDad.geneticCode[indexSeparation:]
                secondGeneticCode = secondDad.geneticCode[:indexSeparation] + firstDad.geneticCode[indexSeparation:]
                if  firstGeneticCode  in newGeneticCodeList:
                    canAdd = False
                
                if  secondGeneticCode  in newGeneticCodeList:
                    canAdd = False

                if canAdd:
                    newGeneticCodeList.append(firstGeneticCode) 
                    newGeneticCodeList.append(secondGeneticCode)    

                
                        
        if len(newGeneticCodeList) > genetic_algorithm.populationSize:
            randomNumber = (random.randint(1,2))
            del newGeneticCodeList[-randomNumber]
        
        return newGeneticCodeList

        
    elif genetic_algorithm.quantityOfCrossing == 2:
        while len(newGeneticCodeList) < genetic_algorithm.populationSize:
            canAdd = True
            probability = random.randint(1,100)

            firstDad = select_chromossome_for_crossover(genetic_algorithm)
            secondDad = select_chromossome_for_crossover(genetic_algorithm)
            #Testing if its the same dad
            while firstDad == secondDad:
                secondDad = select_chromossome_for_crossover(genetic_algorithm)
            
            #Test if the chromossomes can make a crossover. If not, keep the selected dads  for the next generation.
            if probability > genetic_algorithm.crossingProbability:
                newGeneticCodeList.append(firstDad.geneticCode)
                newGeneticCodeList.append(secondDad.geneticCode)

            else:
                #It can't be 0. When we get 0, no separation occurs and It needs to have at least a number higher than the low serapator.
                indexSeparationLow = random.randint(1,(genetic_algorithm.chromossomeSize -2))
                indexSeparationHigh = random.randint(indexSeparationLow + 1,(genetic_algorithm.chromossomeSize -1))

                firstGeneticCode = firstDad.geneticCode[:indexSeparationLow] + secondDad.geneticCode[indexSeparationLow:indexSeparationHigh] + firstDad.geneticCode[indexSeparationHigh:]
                secondGeneticCode = secondDad.geneticCode[:indexSeparationLow] + firstDad.geneticCode[indexSeparationLow:indexSeparationHigh] + secondDad.geneticCode[indexSeparationHigh:]
                
                if  firstGeneticCode  in newGeneticCodeList:
                    canAdd = False
                
                if  secondGeneticCode  in newGeneticCodeList:
                    canAdd = False

                if canAdd:
                    newGeneticCodeList.append(firstGeneticCode) 
                    newGeneticCodeList.append(secondGeneticCode)  
                
        if len(newGeneticCodeList) > genetic_algorithm.populationSize:
            randomNumber = (random.randint(1,2))
            del newGeneticCodeList[-randomNumber]
        return newGeneticCodeList

def make_mutation(genetic_algorithm,cromossome):
    import random
    cromossomeArray = list(cromossome.geneticCode)
    for i in range(len(cromossomeArray)):
        probability = random.randint(1,100)
        
    
        if probability < genetic_algorithm.mutationProbability:
           
            if cromossomeArray[i] == '1':
                cromossomeArray[i] = '0'

            elif cromossomeArray[i] == '0':
                cromossomeArray[i] = '1'
            
        cromossome.geneticCode = "".join(cromossomeArray)

    return cromossome

def get_best_chromossome(chromossomeList):
    bestChromossome = chromossomeList[0]
    for item in chromossomeList:
        if item.fitness >= bestChromossome.fitness:
            bestChromossome = item

    return bestChromossome

def run_tournment_selection(genetic_algoritm):
    newList = []
    for i in range(genetic_algoritm.populationSize/2):
        tournmentResult = make_tournment_selection(genetic_algoritm)
        newChromossomes = make_crossing_with_two_chromossomes(
            tournmentResult['bestChromossome'],
            tournmentResult['secondBestChromossome'], 
            genetic_algoritm.chromossomeSize,
            genetic_algoritm.quantityOfCrossing
        )

        newChromossome1 = Chromossome(newChromossomes['geneA'])
        newChromossome2 = Chromossome(newChromossomes['geneB'])
        
        newList.append(newChromossome1)
        newList.append(newChromossome2)

        print(i, newChromossomes['geneA'], newChromossomes['geneB'])

    return newList


def make_tournment_selection(genetic_algoritm):
    import random
    from project1.model.Chromossome import Chromossome
    selectionList = []
    listOfChromossomes = []
    populationSize = genetic_algoritm.populationSize
    index = 0
    #generating indexes of selection
    for i in range(genetic_algoritm.tournmentSize):
        index = random.randint(0,populationSize-1)
        while index in selectionList:
            index = random.randint(0,populationSize-1)
        selectionList.append(index)
        listOfChromossomes.append(genetic_algoritm.currentChromossomeList[index])

    bestChromossome = Chromossome(0)
    secondBestChromossome = Chromossome(0)
    for item in listOfChromossomes:
        if item.fitness > bestChromossome.fitness:
            secondBestChromossome = bestChromossome
            bestChromossome = item
        elif item.fitness > secondBestChromossome.fitness:
            secondBestChromossome = item
    return {
        'bestChromossome': bestChromossome,
        'secondBestChromossome': secondBestChromossome
    }



def make_crossing_with_two_chromossomes(geneA, geneB, chromossomeSize, quantityCrossing):
    import random
    
    if quantityCrossing == 1:
        indexSeparation = random.randint(1,(chromossomeSize -1))
            
        newGeneA = geneA.geneticCode[:indexSeparation] + geneA.geneticCode[indexSeparation:]
        newGeneB = geneB.geneticCode[:indexSeparation] + geneB.geneticCode[indexSeparation:]
        return {
            'geneA': newGeneA,
            'geneB': newGeneB
        }
    elif quantityCrossing == 2:
        indexSeparationLow = random.randint(1,(chromossomeSize -2))
        indexSeparationHigh = random.randint(indexSeparationLow + 1,(chromossomeSize -1))

        firstGeneticCode = geneA.geneticCode[:indexSeparationLow] + geneB.geneticCode[indexSeparationLow:indexSeparationHigh] + geneA.geneticCode[indexSeparationHigh:]
        secondGeneticCode = geneB.geneticCode[:indexSeparationLow] + geneA.geneticCode[indexSeparationLow:indexSeparationHigh] + geneB.geneticCode[indexSeparationHigh:]
        return {
            'geneA': firstGeneticCode,
            'geneB': secondGeneticCode
        }
    return ""