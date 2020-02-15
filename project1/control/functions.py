
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



def make_crossover(genetic_algoritm):
    import random

    firstChromossome = random.randrange(0, genetic_algoritm.populationSize - 1, 1)
    secondChromossome = random.randrange(0, genetic_algoritm.populationSize - 1, 1)
    while firstChromossome == secondChromossome:
        secondChromossome = random.randrange(0, genetic_algoritm.populationSize - 1, 1)
    
    firstChromossome = genetic_algoritm.currentChromossomeList[firstChromossome].geneticCode
    secondChromossome = genetic_algoritm.currentChromossomeList[secondChromossome].geneticCode

    if genetic_algoritm.quantityOfCrossing == 1:
        firstCrossing = random.randrange(1, genetic_algoritm.chromossomeSize, 1)
        part1 = firstChromossome[:((firstCrossing))]
        part2 = secondChromossome[((firstCrossing)):]
        return part1 + part2
        
    elif genetic_algoritm.quantityOfCrossing == 2:

        firstCrossing = random.randrange(0, genetic_algoritm.chromossomeSize-1, 1)
        secondCrossing = random.randrange(1, genetic_algoritm.chromossomeSize-1, 1)

        while firstCrossing == secondCrossing:
            secondCrossing = random.randrange(1, genetic_algoritm.chromossomeSize-1, 1)
        if firstCrossing > secondCrossing:
            temp = firstCrossing
            firstCrossing = secondCrossing
            secondCrossing = temp
        """
        print(
            firstCrossing, ' - ' ,secondCrossing,
            "\n"
        )
        print(
            firstChromossome, ' - ' ,secondChromossome,
            "\n"
        )
        """
        part1, part3 = firstChromossome[:((firstCrossing))] , firstChromossome[((secondCrossing)):]
        part2 = secondChromossome[((firstCrossing)):((secondCrossing))]
        '''
        print(
            "Cr1 : " + str(firstChromossome) + "\n" +
            "Cr2 : " + str(secondChromossome) +  "\n" +
            "Cr3 : " + str(part1)+str(part2)+str(part3)+ "\n"
        )
        '''
        return part1 + part2 + part3
    

def make_mutation(cromossome):
    
    pass