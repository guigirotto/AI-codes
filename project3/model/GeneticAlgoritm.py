class GeneticAlgoritm:

    current_chromosome_list = []
    best_chromosome = ""
    best_chromosome_generation = ""
    best_chromosome_fitness = 0

    def __init__(
        self,
        chromosome_size=0,
        population_size=0,
        crossing_probability=0,
        mutation_probability=0,
        method_of_selection=0,
        elitism_size=0,
        quantity_of_crossing=0,
        quantity_of_generation=0,
    ):

        self.population_size = int(population_size)
        self.crossing_probability = int(crossing_probability)
        self.mutation_probability = int(mutation_probability)
        self.elitism_size = int(elitism_size)
        self.quantity_of_crossing = int(quantity_of_crossing)
        self.quantity_of_generation = int(quantity_of_generation)
        self.chromosome_size = int(chromosome_size)
        self.method_of_selection = int(method_of_selection)
        self.tournament_size = 0

    def set_tournament_size(self, tournament_size):
        self.tournament_size = int(tournament_size)


    def set_best_chromosome(self, new_chromosome, generation, fitness):
        self.best_chromosome = new_chromosome
        self.best_chromosome_generation = generation
        self.best_chromosome_fitness = fitness
        print(
            "CURRENT BEST CHROMOSOME: "
            + new_chromosome
            + "\nGeneration: "
            + str(generation)
            + "\nFitness: "
            + str(fitness)
        )

    def get_total_fitness(self):
        total = 0.0
        for i in self.current_chromosome_list:
            total += i.fitness
        return total

    def print_chromosomes(self):
        for i in self.current_chromosome_list:
            print(
                str(i.genetic_code)
                + " - F: "
                + str(i.fitness)
                + "- P: "
                + str(i.probability)
                + "- G: "
                + str(i.generation)
            )
