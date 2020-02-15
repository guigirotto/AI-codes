
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
    for i in range(8-len(binaryString)):
        binaryString = "0" + binaryString
    return binaryString

def calculate_fitness(value_x, value_y):
    import math
    result = 21.5 + value_x*math.sin(4*math.pi*value_x) + value_y*math.sin(20*math.pi*value_y)
    return result
    
def calculate_roulette_probability(fitness_value, fitness_summation):
    probability = fitness_value/fitness_summation
    return probability



def make_crossover(genetic_algoritm):
    import random
    newGeneticCodeList=[]
    canAdd = True
    if genetic_algoritm.quantityOfCrossing == 1:
        while len(newGeneticCodeList) < genetic_algoritm.populationSize:
            canAdd = True
            #Need to see if its necessary to put genetic_algoritm.populationSize -1 or just genetic_algoritm.populationSize
            firstDad = genetic_algoritm.currentChromossomeList[random.randint(0,(genetic_algoritm.populationSize -1))]
            secondDad = genetic_algoritm.currentChromossomeList[random.randint(0,(genetic_algoritm.populationSize-1))]
            #Testing if its the same dad
            while firstDad == secondDad:
                secondDad = genetic_algoritm.currentChromossomeList[random.randint(0,genetic_algoritm.populationSize -1)]
            #It can't be 0. When we get 0, no separation occurs
            indexSeparation = random.randint(1,(genetic_algoritm.chromossomeSize -1))
            
            firstGeneticCode = firstDad.geneticCode[:indexSeparation] + secondDad.geneticCode[indexSeparation:]
            secondGeneticCode = secondDad.geneticCode[:indexSeparation] + firstDad.geneticCode[indexSeparation:]
            if  firstGeneticCode  in newGeneticCodeList:
                canAdd = False
            
            if  secondGeneticCode  in newGeneticCodeList:
                canAdd = False

            if canAdd:
                newGeneticCodeList.append(firstGeneticCode) 
                newGeneticCodeList.append(secondGeneticCode)    

                
                        
    
        return newGeneticCodeList

        
    elif genetic_algoritm.quantityOfCrossing == 2:
        while len(newGeneticCodeList) < genetic_algoritm.populationSize:
            canAdd = True
            #Need to see if its necessary to put genetic_algoritm.populationSize -1 or just genetic_algoritm.populationSize
            firstDad = genetic_algoritm.currentChromossomeList[random.randint(0,(genetic_algoritm.populationSize -1))]
            secondDad = genetic_algoritm.currentChromossomeList[random.randint(0,(genetic_algoritm.populationSize-1))]
            #Testing if its the same dad
            while firstDad == secondDad:
                secondDad = genetic_algoritm.currentChromossomeList[random.randint(0,genetic_algoritm.populationSize -1)]
            #It can't be 0. When we get 0, no separation occurs and It needs to have at least a number higher than the low serapator.
            indexSeparationLow = random.randint(1,(genetic_algoritm.chromossomeSize -2))
            indexSeparationHigh = random.randint(indexSeparationLow + 1,(genetic_algoritm.chromossomeSize -1))

            firstGeneticCode = firstDad.geneticCode[:indexSeparationLow] + secondDad.geneticCode[indexSeparationLow:indexSeparationHigh] + firstDad.geneticCode[indexSeparationHigh:]
            secondGeneticCode = secondDad.geneticCode[:indexSeparationLow] + firstDad.geneticCode[indexSeparationLow:indexSeparationHigh] + secondDad.geneticCode[indexSeparationHigh:]
            
            if  firstGeneticCode  in newGeneticCodeList:
                canAdd = False
            
            if  secondGeneticCode  in newGeneticCodeList:
                canAdd = False

            if canAdd:
                newGeneticCodeList.append(firstGeneticCode) 
                newGeneticCodeList.append(secondGeneticCode)  

        return newGeneticCodeList

def make_mutation(genetic_algoritm,cromossome):
    import random
    cromossomeArray = list(cromossome.geneticCode)
    for i in range(len(cromossomeArray)):
        probability = random.randint(1,100)
        
    
        if probability < genetic_algoritm.mutationProbability:
            print("I =" + str(i))
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