import numpy as np
from project3.control.functions import matrix_distances
from project3.control.functions import return_cities
from project3.model.Chromosome import Chromosome



def run_genetic_algoritm_2():
    return_cities()
    teste = Chromosome(return_cities(),1)
    teste.calculate_fitness()
    print(teste.fitness)

