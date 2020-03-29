import numpy as np
from project3.control.functions import *
from project3.model.Chromosome import Chromosome
from project3.model.GeneticAlgoritm import GeneticAlgoritm
from project3.view.result_display import show_chart2


def run_teste():
    cities =['campo_florido', 'prata', 'comendador_gomes', 'perdizes', 'araxa', 'ituiutaba', 'agua_comprida', 'conceicao_das_alagoas', 'frutal', 'sacramento', 'uberlandia', 'santa_juliana', 'campo_florido', 'nova_ponte', 'araguari', 'patrocinio', 'ituiutaba', 'prata', 'campo_florido']
    teste = Chromosome(cities,0)
    teste.calculate_fitness()
    print("primeiro")
    print(1/teste.fitness)
  
def run_genetic_algoritm_2():
    # Use only to test
    print("--- ATENTION: Do not forget to erase the test code input ---- ")
    input_result: GeneticAlgoritm = GeneticAlgoritm(
        chromosome_size=20,
        population_size=50,
        crossing_probability=70,
        mutation_probability=5,
        method_of_selection=1,
        elitism_size=1,
        quantity_of_crossing=2,
        quantity_of_generation=10,
    )
    input_result.set_tournament_size(20)

    if not input_result:
        print("Ops, something went wrong")
        return

    #  generating chromosome list
    best_chromosome_list = []

    input_result.current_chromosome_list = []
    actual_generation = 0

     # converting the chromosome and populate the current list
    for i in range(input_result.population_size):
        new_chromosome = Chromosome(return_cities(),actual_generation)
        new_chromosome.calculate_fitness()
        input_result.current_chromosome_list.append(new_chromosome)
    
    sum_fitness = calculate_fitness_sum(input_result)
    sum_prob = 0

    for index, item in enumerate(input_result.current_chromosome_list):
        if index == 0:
            probability = calculate_roulette_probability(item.fitness, sum_fitness)
            #print(probability)
            item.set_probability(probability)
            sum_prob += probability
        else:
            probability = calculate_roulette_probability(item.fitness, sum_fitness)
            #print(probability)
            sum_prob += probability
            item.set_probability(sum_prob)

    best_chromosome = get_best_chromosome(input_result.current_chromosome_list)
    best_chromosome_list.append(best_chromosome)
    #print('----------------------------------------')
    #for i in input_result.current_chromosome_list:
     #   print(i.probability)
    #print('----------------------------------------')
    actual_generation += 1
    while actual_generation < input_result.quantity_of_generation:
        new_chromosome_list= []
        #crossover
        if input_result.method_of_selection == 1:
          """   for i in range(0,len(input_result.current_chromosome_list),2):
                chromosome_1 = input_result.current_chromosome_list[i]
                chromosome_2 = input_result.current_chromosome_list[i+1]
                chromosome_list_1 = chromosome_1.genetic_code
                chromosome_list_2 = chromosome_2.genetic_code
                lists = make_crossover_ox(chromosome_list_1,chromosome_list_2)
                new_chromosome1 = Chromosome(lists[0],actual_generation)
                new_chromosome2 = Chromosome(lists[1],actual_generation)
                new_chromosome1.calculate_fitness()
                new_chromosome2.calculate_fitness()
                new_chromosome_list.append(new_chromosome1)
                new_chromosome_list.append(new_chromosome2) """
        new_chromosome_list = make_roullete(input_result,actual_generation)
            
        if(input_result.elitism_size > 0):
                elitsm_list = keep_chromosomes_elitism(input_result)
                for i in range(len(elitsm_list)):
                    new_chromosome_list[i] = Chromosome(elitsm_list[i].genetic_code,actual_generation,elitsm_list[i].fitness)
        elif input_result.method_of_selection == 2:
            #  crossover tournament
            crossover_chromosomes_genetic_codes = run_tournament_selection(
                input_result, generation=actual_generation
            )
            for index,item in enumerate(crossover_chromosomes_genetic_codes):
                if not (index < input_result.elitism_size):
                    item.calculate_fitness()

            input_result.current_chromosome_list = (
                crossover_chromosomes_genetic_codes.copy()
            )
            new_chromosome_list = crossover_chromosomes_genetic_codes.copy()
        #List complete

        #  Mutations
        for index, item in enumerate(new_chromosome_list):
            #  Keep the elitism without mutations
            if not (index < input_result.elitism_size):
                new_chromosome_list[index].make_mutation()
              
        
         #  Calculating new fitness after mutations
        for index, item in enumerate(new_chromosome_list):
            #  Keep the elitism without mutations
            if not (index < input_result.elitism_size):
                new_chromosome_list[index].calculate_fitness()

        #  Calculating chromosome probability for the using on the next crossover if its needed
        sum_fitness = calculate_fitness_sum(input_result)
        sum_prob = 0
        for index, item in enumerate(input_result.current_chromosome_list):
            if index == 0:
                probability = calculate_roulette_probability(item.fitness, sum_fitness)
                item.set_probability(probability)
                sum_prob += probability
            else:
                probability = calculate_roulette_probability(item.fitness, sum_fitness)
                sum_prob += probability
                item.set_probability(sum_prob)


        #  Get BestChromosome for each generation
        best_chromosome = get_best_chromosome(new_chromosome_list)
        best_chromosome_list.append(Chromosome(best_chromosome.genetic_code,actual_generation,best_chromosome.fitness))

            
        input_result.current_chromosome_list = new_chromosome_list.copy()
        actual_generation += 1
    
    print('----------------------')
    #for i in range(len(best_chromosome_list)):
    #    print(best_chromosome_list[i].generation, 1 / best_chromosome_list[i].fitness)
     #   print(best_chromosome_list[i].genetic_code)
    print(1 / best_chromosome_list[-1].fitness)
    print('---------------------')
    show_chart2(best_chromosome_list, input_result.quantity_of_generation)

        

