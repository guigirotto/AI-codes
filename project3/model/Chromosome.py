from project3.control.functions import matrix_distances
from project3.control.functions import value_matrix
import numpy as np
import random
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

    def calculate_fitness(self):
        matrix = matrix_distances()
        new_fitness = 0
        for i in range(0,len(self.genetic_code),2):
            city1 = value_matrix(self.genetic_code[i])
            city2 = value_matrix(self.genetic_code[i+1])
            distance = matrix.item((city1,city2))
            new_fitness = new_fitness + distance
        new_fitness = new_fitness + matrix.item((value_matrix(),value_matrix(self.genetic_code[0])))
        new_fitness = new_fitness + matrix.item((value_matrix(self.genetic_code[19]),value_matrix()))
        self.fitness = new_fitness

    def make_mutation(self):
        position_1 = random.randint(0,19)
        position_2 = random.randint(0,19)
        if(position_1 != position_2):
            aux1 = self.genetic_code[position_1]
            aux2 = self.genetic_code[position_2]
            self.genetic_code[position_2] = aux1
            self.genetic_code[position_1] = aux2