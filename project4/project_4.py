#
# Artificial intelligence - Project 4
# Computer Engineering - Semester 9
# Genetic Algoritm With real chromosome - Using Roullete or Tornament method
# Date February 09, 2020
#
from project4.view.result_display import show_chart
from project4.view.result_display import show_chart2
from project4.model.GeneticAlgoritm import GeneticAlgoritm
import random
from project4.control.functions import *


def run_genetic_algoritm():
    # creating genetic algoritm object class
    #  inputResult = get_values_from_user()

    # Use only to test
    print("---ATENTION: Do not forget to erase the test code input ---- ")
    input_result: GeneticAlgoritm = GeneticAlgoritm(
        chromosome_size=2,
        population_size=50,
        crossing_probability=40,
        mutation_probability=80,
        method_of_selection=2,
        elitism_size=1,
        method_of_crossing=1,
        quantity_of_generation=50,
    )
    input_result.set_tournament_size(16)

    if not input_result:
        print("Ops, something went wrong")
        return

    #  generating chromosome list
    chromosome_real_list = []
    best_chromosome_list = []

    max_value = 2 ** input_result.chromosome_size
    for item in range(int(input_result.population_size)):
        initial_genetic_code = []
        for i in range(input_result.chromosome_size):
            random_value_gene = random.random()
            initial_genetic_code.append(random_value_gene)

        chromosome_real_list.append(initial_genetic_code)

    input_result.current_chromosome_list = []
    actual_generation = 0

    # converting the chromosome and populate the current list
    for item in chromosome_real_list:
        new_chromosome = Chromosome(genetic_code=item, generation=actual_generation)

        real_x = input_result.get_conversion_from_gene_to_real(
            new_chromosome.genetic_code[0]
        )
        real_y = input_result.get_conversion_from_gene_to_real(
            new_chromosome.genetic_code[1]
        )

        fitness = calculate_fitness(real_x, real_y)
        new_chromosome.set_fitness(fitness)

        input_result.current_chromosome_list.append(new_chromosome)

    sum_fitness = calculate_fitness_sum(input_result)
    sum_fitness_delta = calculate_fitness_delta(input_result, sum_fitness)
    sum_prob = 0

    for index, item in enumerate(input_result.current_chromosome_list):
        if index == 0:
            probability = calculate_roulette_probability(
                item.fitness, sum_fitness, sum_fitness_delta
            )
            item.set_probability(probability)
            sum_prob += probability
        else:
            probability = calculate_roulette_probability(
                item.fitness, sum_fitness, sum_fitness_delta
            )
            sum_prob += probability
            item.set_probability(sum_prob)

    best_chromosome = get_best_chromosome(input_result.current_chromosome_list)
    best_chromosome_list.append(best_chromosome)

    actual_generation += 1
    while actual_generation < input_result.quantity_of_generation:
        print(f"Generation {actual_generation}")
        new_chromosome_list = []

        #  Crossover
        if input_result.method_of_selection == 1:
            crossover_chromosomes_genetic_codes = make_crossover(
                input_result, generation=actual_generation
            )
            #  Need to create chromosome and add on the new list
            for new_chromosome in crossover_chromosomes_genetic_codes:

                gene_x = new_chromosome.genetic_code[0]
                gene_y = new_chromosome.genetic_code[1]
                real_x = input_result.get_conversion_from_gene_to_real(gene_x)
                real_y = input_result.get_conversion_from_gene_to_real(gene_y)
                fitness = calculate_fitness(real_x, real_y)

                new_chromosome.set_fitness(fitness)
                new_chromosome_list.append(new_chromosome)

            input_result.current_chromosome_list = new_chromosome_list

        elif input_result.method_of_selection == 2:
            #  crossover tournament
            crossover_chromosomes_genetic_codes = run_tournament_selection(
                input_result, generation=actual_generation
            )
            for item in crossover_chromosomes_genetic_codes:

                gene_x = item.genetic_code[0]
                gene_y = item.genetic_code[1]
                real_x = input_result.get_conversion_from_gene_to_real(gene_x)
                real_y = input_result.get_conversion_from_gene_to_real(gene_y)
                fitness = calculate_fitness(real_x, real_y)

                item.set_fitness(fitness)

            input_result.current_chromosome_list = crossover_chromosomes_genetic_codes
        # list complete

        #  Mutations
        for index, item in enumerate(input_result.current_chromosome_list):
            #  Keep the elitism without mutations
            if not (index < input_result.elitism_size):
                item = make_mutation(input_result, item)

        #  Calculating new fitness after mutations
        for item in input_result.current_chromosome_list:
            gene_x = item.genetic_code[0]
            gene_y = item.genetic_code[1]
            real_x = input_result.get_conversion_from_gene_to_real(gene_x)
            real_y = input_result.get_conversion_from_gene_to_real(gene_y)
            fitness = calculate_fitness(real_x, real_y)
            item.set_fitness(fitness)

        #  Calculating chromosome probability for the using on the next crossover if its needed
        sum_fitness = calculate_fitness_sum(input_result)
        sum_fitness_delta = calculate_fitness_delta(input_result, sum_fitness)
        sum_prob = 0
        for index, item in enumerate(input_result.current_chromosome_list):
            if index == 0:
                probability = calculate_roulette_probability(
                    item.fitness, sum_fitness, sum_fitness_delta
                )
                item.set_probability(probability)
                sum_prob += probability
            else:
                probability = calculate_roulette_probability(
                    item.fitness, sum_fitness, sum_fitness_delta
                )
                sum_prob += probability
                item.set_probability(sum_prob)

        #  Get BestChromosome for each generation
        best_chromosome_generation = get_best_chromosome(
            input_result.current_chromosome_list
        )

        best_chromosome = best_chromosome_generation
        best_chromosome_list.append(best_chromosome)

        actual_generation += 1

    #  End while
    print("\n\n\n----------- Last Population-----------------")
    print(input_result.print_chromosomes())
    print("\n\n\n ------------RESULT---------------- \n")
    for best_chromosome in best_chromosome_list:
        print(
            f"Gen: {best_chromosome.generation} Genetic code: {best_chromosome.genetic_code} Fitness: {best_chromosome.fitness}"
        )

    show_chart(best_chromosome_list, input_result)
    show_chart2(best_chromosome_list, input_result.quantity_of_generation)
