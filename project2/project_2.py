#
# Artificial intelligence - Project 2
# Computer Engineering - Semester 9
# Genetic Algoritm - Using Roullete or Tornament method
# Date February 09, 2020
#
from project2.view.result_display import show_chart
from project2.view.result_display import show_chart2
from project2.model.GeneticAlgoritm import GeneticAlgoritm
import random
from project2.control.functions import *


def test():
    from project2.model.Pair import Pair

    cr_a = Chromosome(
        generation=0,
        genetic_code=[
            Pair(pair_id=1),
            Pair(pair_id=5),
            Pair(pair_id=4),
            Pair(pair_id=3),
            Pair(pair_id=2),
            Pair(pair_id=5),
            Pair(pair_id=4),
            Pair(pair_id=1),
            Pair(pair_id=3),
            Pair(pair_id=2),
            Pair(pair_id=4),
            Pair(pair_id=1),
            Pair(pair_id=5),
            Pair(pair_id=2),
            Pair(pair_id=3),
            Pair(pair_id=4),
            Pair(pair_id=1),
            Pair(pair_id=5),
            Pair(pair_id=2),
            Pair(pair_id=3),
            Pair(pair_id=1),
        ],
    )
    print(cr_a.check_if_genetic_code_is_valid())
    cr_a.calculate_fitness()


def run_genetic_algoritm_1():
    # creating genetic algoritm object class
    #  inputResult = get_values_from_user()

    # Use only to test
    print("--- ATENTION: Do not forget to erase the test code input ---- ")
    input_result: GeneticAlgoritm = GeneticAlgoritm(
        chromosome_size=21,
        population_size=100,
        crossing_probability=30,
        mutation_probability=60,
        method_of_selection=2,
        elitism_size=4,
        quantity_of_crossing=2,
        quantity_of_generation=100,
    )
    input_result.set_tournament_size(10)

    if not input_result:
        print("Ops, something went wrong")
        return

    #  generating chromosome list
    best_chromosome_list = []

    input_result.current_chromosome_list = []
    actual_generation = 0

    # converting the chromosome and populate the current list
    for i in range(input_result.population_size):
        new_chromosome = Chromosome(generation=actual_generation)
        new_chromosome.create_really_random_genetic_code()
        fitness = new_chromosome.calculate_fitness()
        new_chromosome.set_fitness(fitness)
        input_result.current_chromosome_list.append(new_chromosome)

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

    best_chromosome = get_best_chromosome(input_result.current_chromosome_list)
    best_chromosome_list.append(best_chromosome)

    actual_generation += 1
    while actual_generation < input_result.quantity_of_generation:
        if True:
            print(f"\n Gen: {actual_generation}\n")
            for i in input_result.current_chromosome_list:
                print(i.fitness)
            print("\n\n")
        new_chromosome_list = []

        #  Crossover
        if input_result.method_of_selection == 1:
            crossover_chromosomes_genetic_codes = make_crossover(
                input_result, generation=actual_generation
            )
            #  Need to create chromosome and add on the new list
            for new_chromosome in crossover_chromosomes_genetic_codes:
                fitness = new_chromosome.calculate_fitness()
                new_chromosome.set_fitness(fitness)
                new_chromosome_list.append(new_chromosome)

            input_result.current_chromosome_list = new_chromosome_list.copy()

        elif input_result.method_of_selection == 2:
            #  crossover tournament
            crossover_chromosomes_genetic_codes = run_tournament_selection(
                input_result, generation=actual_generation
            )
            for item in crossover_chromosomes_genetic_codes:
                fitness = item.calculate_fitness()
                item.set_fitness(fitness)

            input_result.current_chromosome_list = (
                crossover_chromosomes_genetic_codes.copy()
            )
        # list complete

        #  Mutations
        for index, item in enumerate(input_result.current_chromosome_list):
            #  Keep the elitism without mutations
            if not (index < input_result.elitism_size):
                item = make_mutation(input_result, item)

        #  Calculating new fitness after mutations
        for item in input_result.current_chromosome_list:
            fitness = item.calculate_fitness()
            item.set_fitness(fitness)

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
        best_chromosome_generation = get_best_chromosome(
            input_result.current_chromosome_list
        )

        best_chromosome = best_chromosome_generation
        best_chromosome_list.append(best_chromosome)

        actual_generation += 1
    if True:
        #  End while
        # print("\n\n\n----------- Last Population-----------------")
        # print(input_result.print_chromosomes())
        # print("\n\n\n ------------RESULT---------------- \n")
        for best_chromosome in best_chromosome_list:
            if best_chromosome.check_if_genetic_code_is_valid()["valid"]:
                print(
                    "CURRENT BEST CHR0MOSOME: "
                    + "\tGeneration: "
                    + str(best_chromosome.generation)
                    + "\tFitness: "
                    + str(best_chromosome.fitness)
                )
                best_chromosome.print_scale()
    print(best_chromosome.print_scale())
    #    show_chart(best_chromosome_list, input_result)
    show_chart2(best_chromosome_list, input_result.quantity_of_generation)
