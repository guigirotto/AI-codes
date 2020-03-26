import numpy as np
from project3.control.functions import *
from project3.model.Chromosome import Chromosome
from project3.model.GeneticAlgoritm import GeneticAlgoritm
from project3.view.result_display import show_chart2



def run_genetic_algoritm_2():
    # Use only to test
    print("--- ATENTION: Do not forget to erase the test code input ---- ")
    input_result: GeneticAlgoritm = GeneticAlgoritm(
        chromosome_size=20,
        population_size=50,
        crossing_probability=70,
        mutation_probability=5,
        method_of_selection=1,
        elitism_size=0,
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

    best_chromosome = get_best_chromosome(input_result.current_chromosome_list)
    best_chromosome_list.append(best_chromosome)

    actual_generation += 1
    while actual_generation < input_result.quantity_of_generation:
        new_chromosome_list= []
        #crossover
        for i in range(0,len(input_result.current_chromosome_list),2):
            chromosome_1 = input_result.current_chromosome_list[i]
            chromosome_2 = input_result.current_chromosome_list[i+1]
            chromosome_list_1 = chromosome_1.genetic_code
            chromosome_list_2 = chromosome_2.genetic_code
            make_crossover_ox(chromosome_list_1,chromosome_list_2)
            chromosome_1.calculate_fitness()
            chromosome_2.calculate_fitness()
            new_chromosome_list.append(chromosome_1)
            new_chromosome_list.append(chromosome_2)

        input_result.current_chromosome_list = new_chromosome_list.copy()
        
        #  Get BestChromosome for each generation
        best_chromosome = get_best_chromosome(input_result.current_chromosome_list)
        best_chromosome.set_generation(actual_generation)
        print(best_chromosome.generation, best_chromosome.fitness)
        best_chromosome_list.append(best_chromosome)

        actual_generation += 1
    print('----------------------')
    for i in range(len(best_chromosome_list)):
        print(best_chromosome_list[i].generation, best_chromosome_list[i].fitness)
    print('---------------------')
    show_chart2(best_chromosome_list, input_result.quantity_of_generation)

        

