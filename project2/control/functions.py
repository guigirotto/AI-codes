from project2.model.Chromosome import Chromosome


def check_if_user_type_only_digits(
    chromosome_size,
    population_size,
    crossing_probability,
    mutation_probability,
    method_of_selection,
    elitism_size,
    quantity_of_crossing,
    quantity_of_generation,
):
    if not chromosome_size.isdigit():
        return False
    if not population_size.isdigit():
        return False
    if not crossing_probability.isdigit():
        return False
    if not mutation_probability.isdigit():
        return False
    if not method_of_selection.isdigit():
        return False
    if not elitism_size.isdigit():
        return False
    if not quantity_of_crossing.isdigit():
        return False
    if not quantity_of_generation.isdigit():
        return False
    return True


def format_binary_code(binary_code, chromosome_size):
    #  getting only the binary part of 0b0101010
    binary_string = str(binary_code).split("b")[1]
    for i in range(chromosome_size - len(binary_string)):
        binary_string = "0" + binary_string
    return binary_string


def calculate_fitness(value_x, value_y):
    import math

    result = (
        21.5
        + value_x * math.sin(4 * math.pi * value_x)
        + value_y * math.sin(20 * math.pi * value_y)
    )
    return result


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


def keep_chromosomes_elitism(genetic_algorithm):
    chromosome_list = genetic_algorithm.current_chromosome_list.copy()
    chromosome_to_still_list = []
    while len(chromosome_to_still_list) < genetic_algorithm.elitism_size:
        best_chromosome = get_best_chromosome(chromosome_list)
        chromosome_list.remove(best_chromosome)
        chromosome_to_still_list.append(best_chromosome)

    return chromosome_to_still_list


def make_crossover(genetic_algorithm, generation):
    import random

    can_add = True
    new_genetic_code_list = []

    if genetic_algorithm.elitism_size > 0:
        chromosomes_list = keep_chromosomes_elitism(genetic_algorithm)
        for i in chromosomes_list:
            new_genetic_code_list.append(i.genetic_code)
    else:
        chromosomes_list = []

    if genetic_algorithm.quantity_of_crossing == 1:
        while len(new_genetic_code_list) < genetic_algorithm.population_size:
            can_add = True
            probability = random.randint(1, 100)

            first_dad = select_chromosome_for_crossover(genetic_algorithm)
            second_dad = select_chromosome_for_crossover(genetic_algorithm)
            # Testing if it is the same dad
            while first_dad == second_dad:
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
                index_separation = random.randint(
                    1, (genetic_algorithm.chromosome_size - 1)
                )

                first_genetic_code = (
                    first_dad.genetic_code[:index_separation]
                    + second_dad.genetic_code[index_separation:]
                )
                second_genetic_code = (
                    second_dad.genetic_code[:index_separation]
                    + first_dad.genetic_code[index_separation:]
                )
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
                chromosomes_list.append(new_chromosome)

        return chromosomes_list

    elif genetic_algorithm.quantity_of_crossing == 2:
        while len(new_genetic_code_list) < genetic_algorithm.population_size:
            can_add = True
            probability = random.randint(1, 100)

            first_dad = select_chromosome_for_crossover(genetic_algorithm)
            second_dad = select_chromosome_for_crossover(genetic_algorithm)
            # Testing if its the same dad
            while first_dad == second_dad:
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
                # It can't be 0. When we get 0, no separation occurs and It needs to have at least a number higher
                # than the low separator.
                index_separation_low = random.randint(
                    1, (genetic_algorithm.chromosome_size - 2)
                )
                index_separation_high = random.randint(
                    index_separation_low + 1, (genetic_algorithm.chromosome_size - 1)
                )

                first_genetic_code = (
                    first_dad.genetic_code[:index_separation_low]
                    + second_dad.genetic_code[
                        index_separation_low:index_separation_high
                    ]
                    + first_dad.genetic_code[index_separation_high:]
                )
                second_genetic_code = (
                    second_dad.genetic_code[:index_separation_low]
                    + first_dad.genetic_code[index_separation_low:index_separation_high]
                    + second_dad.genetic_code[index_separation_high:]
                )

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
                chromosomes_list.append(new_chromosome)

        return chromosomes_list


def make_mutation(genetic_algorithm, chromosome):
    from project2.model.Pair import Pair
    import random

    list_of_pairs = [
        Pair(pair_id=1, employee_1=1, employee_2=2),
        Pair(pair_id=2, employee_1=3, employee_2=4),
        Pair(pair_id=3, employee_1=5, employee_2=6),
        Pair(pair_id=4, employee_1=7, employee_2=8),
        Pair(pair_id=5, employee_1=9, employee_2=10),
    ]
    for index, item in enumerate(chromosome.genetic_code, start=0):
        probability = random.randint(1, 100)
        if probability < genetic_algorithm.mutation_probability:
            random_index = random.randint(0, 4)
            item = list_of_pairs[random_index]

    return chromosome


def get_best_chromosome(chromosome_list):
    best_chromosome = chromosome_list[0]
    for item in chromosome_list:
        if item.fitness >= best_chromosome.fitness:
            best_chromosome = item

    return best_chromosome


def run_tournament_selection(genetic_algoritm, generation):
    import random

    new_list = []
    if genetic_algoritm.elitism_size > 0:
        chromosomes_list = keep_chromosomes_elitism(genetic_algoritm)
        for i in chromosomes_list:
            new_list.append(i)

    for i in range(int(genetic_algoritm.population_size / 2)):
        tournament_result = make_tournament_selection(genetic_algoritm)
        new_chromosomes = make_crossing_with_two_chromosomes(
            tournament_result["best_chromosome"],
            tournament_result["second_best_chromosome"],
            genetic_algoritm.chromosome_size,
            genetic_algoritm.quantity_of_crossing,
        )

        new_chromosome1 = Chromosome(new_chromosomes["gene_a"], generation)
        new_chromosome2 = Chromosome(new_chromosomes["gene_b"], generation)

        new_list.append(new_chromosome1)
        new_list.append(new_chromosome2)

        # print(i, new_chromosomes['gene_a'], new_chromosomes['gene_b'])

    if len(new_list) > genetic_algoritm.population_size:
        random_number = random.randint(1, 2)
        del new_list[-random_number]

    return new_list


def make_tournament_selection(genetic_algoritmh):
    import random

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

    best_chromosome = Chromosome(0, 0)
    second_best_chromosome = Chromosome(0, 0)
    for item in list_of_chromosomes:
        if item.fitness > best_chromosome.fitness:
            second_best_chromosome = best_chromosome
            best_chromosome = item
        elif item.fitness > second_best_chromosome.fitness:
            second_best_chromosome = item
    return {
        "best_chromosome": best_chromosome,
        "second_best_chromosome": second_best_chromosome,
    }


def make_crossing_with_two_chromosomes(
    gene_a, gene_b, chromosome_size, quantity_of_crossing
):
    import random

    if quantity_of_crossing == 1:
        index_separation = random.randint(1, (chromosome_size - 1))

        new_gene_a = (
            gene_a.genetic_code[:index_separation]
            + gene_b.genetic_code[index_separation:]
        )
        new_gene_b = (
            gene_b.genetic_code[:index_separation]
            + gene_a.genetic_code[index_separation:]
        )
        return {"gene_a": new_gene_a, "gene_b": new_gene_b}
    elif quantity_of_crossing == 2:
        index_separation_low = random.randint(1, (chromosome_size - 2))
        index_separation_high = random.randint(
            index_separation_low + 1, (chromosome_size - 1)
        )

        first_genetic_code = (
            gene_a.genetic_code[:index_separation_low]
            + gene_b.genetic_code[index_separation_low:index_separation_high]
            + gene_a.genetic_code[index_separation_high:]
        )
        second_genetic_code = (
            gene_b.genetic_code[:index_separation_low]
            + gene_a.genetic_code[index_separation_low:index_separation_high]
            + gene_b.genetic_code[index_separation_high:]
        )
        return {"gene_a": first_genetic_code, "gene_b": second_genetic_code}
    return ""
