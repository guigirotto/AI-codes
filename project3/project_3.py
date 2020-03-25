import numpy as np
from project3.control.functions import *
from project3.model.Chromosome import Chromosome



def run_genetic_algoritm_2():
    list1 = return_cities()
    list2 = return_cities()
    make_crossover_ox(list1,list2)
