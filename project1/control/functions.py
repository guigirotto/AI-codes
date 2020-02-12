def get_values_from_user():
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
    return check_if_user_type_only_digits(chromossomeSize, populationSize, crossingProbability,
                                     mutationProbability, methodOfSelection, elitismSize,
                                     quantityOfCrossing, quantityOfGeneration)


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

