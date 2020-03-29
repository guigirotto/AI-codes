import numpy as np
import random


def matrix_distances():
    c1 = [ 0, 108, 117, 251, 180, 150, 141, 245, 149, 131, 65, 73, 126, 100, 76, 34, 47, 80, 61, 138 ]
    c2 = [ 108, 0 , 177, 221, 150, 108, 39, 137, 87, 182, 166, 174, 135, 110, 74, 141, 148, 158, 168, 150 ]
    c3 = [ 117, 177, 0, 161, 107, 185, 210, 313, 263, 251, 178, 187, 56, 91, 110, 142, 160, 86, 116, 252 ]
    c4 = [ 251, 221, 161, 0, 75, 153, 219, 357, 312, 405, 332, 341, 139, 188, 180, 296, 314, 251, 272, 375 ]
    c5 = [ 180, 150, 107, 75, 0, 82, 148, 286, 241, 328, 256, 264, 63, 111, 109, 220, 238, 151, 172, 304 ]
    c6 = [ 150, 108, 185, 153, 82, 0, 100, 245, 199, 290, 218, 227, 140, 118, 72, 182, 200, 165, 186, 262 ]
    c7 = [ 141, 39, 210, 219, 148, 100, 0, 171, 125, 220, 198, 206, 167, 142, 116, 173, 180, 218, 200, 188 ]
    c8 = [ 245, 137, 313, 357, 286, 245, 171, 0, 103, 199, 209, 175, 270, 245, 209, 277, 284, 293, 304, 151 ]
    c9 = [ 149, 87, 263, 312, 241, 199, 125, 103, 0, 101, 111, 77, 225, 200, 164, 177, 184, 222, 204, 69 ]
    c10 = [ 131, 182, 251, 405, 328, 290, 220, 199, 101, 0, 75, 76, 266, 227, 216, 165, 122, 210, 192, 52 ]
    c11 = [ 65, 166, 178, 332, 256, 218, 198, 209, 111, 75, 0, 35, 193, 168, 144, 93, 50, 141, 120, 100 ]
    c12 = [ 73, 174, 187, 341, 264, 227, 206, 175, 77, 76, 35, 0, 202, 177, 152, 101, 108, 150, 128, 66 ]
    c13 = [ 126, 135, 56, 139, 63, 140, 167, 270, 225, 266, 193, 202, 0, 49, 68, 158, 175, 89, 110, 267 ]
    c14 = [ 100, 110, 91, 188, 111, 118, 142, 245, 200, 227, 168, 177, 49, 0, 43, 119, 137, 72, 93, 229 ]
    c15 = [ 76, 74, 110, 180, 109, 72, 116, 209, 164, 216, 144, 152, 68, 43, 0, 107, 125, 91, 112, 217 ]
    c16 = [ 34, 141, 142, 296, 220, 182, 173, 277, 177, 165, 93, 101, 158, 119, 107, 0, 74, 51, 33, 166 ]
    c17 = [ 47, 148, 160, 314, 238, 200, 180, 284, 184, 122, 50, 108, 175, 137, 125, 74, 0, 123, 101, 170 ]
    c18 = [ 80, 158, 86, 251, 151, 165, 218, 293, 222, 210, 141, 150, 89, 72, 91, 51, 123, 0, 24, 211 ]
    c19 = [ 61, 168, 116, 272, 172, 186, 200, 304, 204, 192, 120, 128, 110, 93, 112, 33, 101, 24, 0, 193 ]
    c20 = [ 138, 150, 252, 375, 304, 262, 188, 151, 69, 52, 100, 66, 267, 229, 217, 166, 170, 211, 193, 0 ] 
    result = np.matrix([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20])
    #print(result.item((value_matrix(),value_matrix('perdizes'))))
    return result

def value_matrix(city="uberaba"):
    cities= {}
    cities['uberaba'] = 0
    cities['uberlandia'] = 1
    cities['araxa'] = 2
    cities['patos_de_minas'] = 3
    cities['patrocinio'] = 4
    cities['monte_carmelo'] = 5
    cities['araguari'] = 6
    cities['ituiutaba'] = 7
    cities['prata'] = 8
    cities['frutal'] = 9
    cities['conceicao_das_alagoas'] = 10
    cities['campo_florido'] = 11
    cities['perdizes'] = 12
    cities['santa_juliana'] = 13
    cities['nova_ponte'] = 14
    cities['delta'] = 15
    cities['agua_comprida'] = 16
    cities['sacramento'] = 17
    cities['conquista'] = 18
    cities['comendador_gomes'] = 19

    return cities[city]

def return_cities():
    cities = ['uberlandia','araxa','patos_de_minas','patrocinio','monte_carmelo','araguari','ituiutaba','prata',
    'frutal','conceicao_das_alagoas','campo_florido','perdizes','santa_juliana','nova_ponte','delta','agua_comprida',
    'sacramento','conquista','comendador_gomes']
    for i in range(len(cities)):
        n = random.randint(0,18)
        aux = cities[n]
        aux2 = cities[i]
        cities[n] = aux2
        cities[i] = aux
    #print(cities)
    return cities

def verify_list(chromosomes_list):
    cities= {}
    cities['uberlandia'] = 0
    cities['araxa'] = 0
    cities['patos_de_minas'] = 0
    cities['patrocinio'] = 0
    cities['monte_carmelo'] = 0
    cities['araguari'] = 0
    cities['ituiutaba'] = 0
    cities['prata'] = 0
    cities['frutal'] = 0
    cities['conceicao_das_alagoas'] = 0
    cities['campo_florido'] = 0
    cities['perdizes'] = 0
    cities['santa_juliana'] = 0
    cities['nova_ponte'] = 0
    cities['delta'] = 0
    cities['agua_comprida'] = 0
    cities['sacramento'] = 0
    cities['conquista'] = 0
    cities['comendador_gomes'] = 0
    newList = chromosomes_list.copy()
    for i in range(len(newList)):
        cities[newList[i]] = cities[newList[i]] + 1
    #print(cities)
    repeat = []
    empty = []

    for key,value in cities.items():
        if(value > 1):
            repeat.append(key)
        elif (value == 0):
            empty.append(key)

    
    for i in range(len(repeat)):
       for j in range(len(newList)):
           if(repeat[i] == newList[j]):
               newList[j]=empty[i]
               break
   #print('------------------------')
    for i in range(len(newList)):
        cities[newList[i]] = cities[newList[i]] + 1
    #print(cities)
    return newList

    
def get_best_chromosome(chromosomes_list):
    best_chromosome = chromosomes_list[0]
    for i in range(len(chromosomes_list)):
        if(chromosomes_list[i].fitness >= best_chromosome.fitness):
            best_chromosome = chromosomes_list[i]
    return best_chromosome
    
def keep_chromosomes_elitism(genetic_algorithm):
    chromosome_list = genetic_algorithm.current_chromosome_list.copy()
    chromosome_to_still_list = []
    while len(chromosome_to_still_list) < genetic_algorithm.elitism_size:
        best_chromosome = get_best_chromosome(chromosome_list)
        chromosome_list.remove(best_chromosome)
        chromosome_to_still_list.append(best_chromosome)

    return chromosome_to_still_list
    
def make_crossover_ox(chromosomes_list1,chromosomes_list2):
    random1 = random.randint(0,18)
    random2 = random.randint(0,18)
    sublist1 = []
    sublist2 = []
    if(random1 < random2):
        sublist1 = chromosomes_list1[random1:random2]
        sublist2 = chromosomes_list2[random1:random2]
        chromosomes_list1[random1:random2] = sublist2
        chromosomes_list2[random1:random2] = sublist1
    else:

        sublist1 = chromosomes_list1[random2:random1]
        sublist2 = chromosomes_list2[random2:random1]
        chromosomes_list1[random2:random1] = sublist2
        chromosomes_list2[random2:random1] = sublist1
    chromosomes_list1 = verify_list(chromosomes_list1)
    chromosomes_list2 = verify_list(chromosomes_list2)
    list_return1 = chromosomes_list1.copy()
    list_return2 = chromosomes_list2.copy()

    return [list_return1,list_return2]

    
def make_tournament_selection(genetic_algoritmh):
    from project3.model.Chromosome import Chromosome
    selection_list = []
    list_of_chromosomes = []
    population_size = genetic_algoritmh.population_size
    index = 0
    # generating indexes of selection
    for i in range(genetic_algoritmh.tournament_size):
        index = random.randint(0, population_size - 1)
        while index in selection_list:
            index = random.randint(0, population_size - 1)
        selection_list.append(index)
        list_of_chromosomes.append(genetic_algoritmh.current_chromosome_list[index])

    best_chromosome = Chromosome([], 0)
    second_best_chromosome = Chromosome([], 0)
    for item in list_of_chromosomes:
        if item.fitness > best_chromosome.fitness:
            second_best_chromosome = best_chromosome
            best_chromosome = item
        elif item.fitness > second_best_chromosome.fitness:
            second_best_chromosome = item
    return [ best_chromosome, second_best_chromosome ]

def run_tournament_selection(genetic_algoritm, generation):
    from project3.model.Chromosome import Chromosome
    new_list = []
    if genetic_algoritm.elitism_size > 0:
        chromosomes_list = keep_chromosomes_elitism(genetic_algoritm)
        for i in chromosomes_list:
            new_list.append(Chromosome(i.genetic_code,i.generation,i.fitness))

    for i in range(int(genetic_algoritm.population_size / 2)):
        tournament_result = make_tournament_selection(genetic_algoritm)
        new_chromosomes = make_crossover_ox(tournament_result[0].genetic_code,tournament_result[1].genetic_code)

        new_chromosome1 = Chromosome(new_chromosomes[0], generation)
        new_chromosome2 = Chromosome(new_chromosomes[1], generation)

        new_list.append(new_chromosome1)
        new_list.append(new_chromosome2)

        # print(i, new_chromosomes['gene_a'], new_chromosomes['gene_b'])

    if len(new_list) > genetic_algoritm.population_size:
        random_number = random.randint(1, 2)
        del new_list[-random_number]

    return new_list

def calculate_roulette_probability(fitness_value, fitness_summation):
    probability = fitness_value / fitness_summation
    return probability

def calculate_fitness_sum(genetic_algorithm):
    sum_fitness = 0
    for item in genetic_algorithm.current_chromosome_list:
        sum_fitness += item.fitness
    return sum_fitness

def select_chromosome_for_crossover(genetic_algorithm):
    import random

    selected_prob = random.uniform(0, 1)
    selected_chromosome = None
    for index, item in enumerate(genetic_algorithm.current_chromosome_list):
        if index == 0:
            if 0 <= selected_prob < item.probability:
                selected_chromosome = item
        elif item == genetic_algorithm.current_chromosome_list[-1]:
            if (
                genetic_algorithm.current_chromosome_list[index - 1].probability
                <= selected_prob
                <= 1
            ):
                selected_chromosome = item
        else:
            if (
                genetic_algorithm.current_chromosome_list[index - 1].probability
                <= selected_prob
                < item.probability
            ):
                selected_chromosome = item

    return selected_chromosome

def make_roullete(genetic_algorithm,generation):
    from project3.model.Chromosome import Chromosome
    chromosomes_list = []
    can_add = True
    new_genetic_code_list = []
    while len(new_genetic_code_list) < genetic_algorithm.population_size:
            can_add = True
            probability = random.randint(1, 100)

            first_dad = select_chromosome_for_crossover(genetic_algorithm)
            second_dad = select_chromosome_for_crossover(genetic_algorithm)
            # Testing if it is the same dad
            while first_dad == second_dad:
                #print(first_dad.probability)
                second_dad = select_chromosome_for_crossover(genetic_algorithm)

            # Test if the chromosomes can make a crossover. If not, keep the selected dads  for the next generation.
            if probability > genetic_algorithm.crossing_probability:
                if first_dad.genetic_code in new_genetic_code_list:
                    can_add = False

                if second_dad.genetic_code in new_genetic_code_list:
                    can_add = False

                if can_add:
                    new_genetic_code_list.append(first_dad.genetic_code)
                    new_genetic_code_list.append(second_dad.genetic_code)

            else:
                # It can't be 0. When we get 0, no separation occurs
                newList = make_crossover_ox(first_dad.genetic_code,second_dad.genetic_code)

                first_genetic_code = newList[0]
                second_genetic_code = newList[1]
                
                if first_genetic_code in new_genetic_code_list:
                    can_add = False

                if second_genetic_code in new_genetic_code_list:
                    can_add = False

                if can_add:
                    new_genetic_code_list.append(first_genetic_code)
                    new_genetic_code_list.append(second_genetic_code)

    if len(new_genetic_code_list) > genetic_algorithm.population_size:
            random_number = random.randint(1, 2)
            del new_genetic_code_list[-random_number]

    for index, item in enumerate(new_genetic_code_list):
            if not (index < genetic_algorithm.elitism_size):
                new_chromosome = Chromosome(item, generation)
                new_chromosome.calculate_fitness()
                chromosomes_list.append(new_chromosome)

    return chromosomes_list
