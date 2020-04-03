class Chromosome:
    def __init__(self, genetic_code=[], generation=0):
        self.genetic_code = genetic_code
        self.fitness = 0
        self.generation = generation
        self.probability = 0

    def set_fitness(self, new_fitness):
        self.fitness = new_fitness

    def set_probability(self, new_probability):
        self.probability = new_probability
