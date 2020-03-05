from project2.control.functions import check_if_user_type_only_digits
from project2.model.GeneticAlgoritm import GeneticAlgoritm


def get_values_from_user():
    chromosome_size = input("Inform a chromosome size: ")
    population_size = input("Inform a population size: ")
    crossing_probability = input("Inform a crossing possibility: ")
    mutation_probability = input("Inform a mutation probability: ")
    quantity_of_generation = input("Inform the quantity of generations: ")
    method_of_selection = input(
        "Inform a selection method to the algoritm \n 1 - Roullete \n 2 - Tournment \n"
    )
    if not (
        method_of_selection.isdigit()
        and (method_of_selection == "1" or method_of_selection == "2")
    ):
        print("Invalid option !")
        return False
    tournament_size = 0
    if method_of_selection == "2":
        tournament_size = input("Inform the tournment size: ")
    elitism_size = input("Inform the elitism size: ")
    quantity_of_crossing = input("Inform the quantity of crossing: ")
    result_of_check = check_if_user_type_only_digits(
        chromosome_size,
        population_size,
        crossing_probability,
        mutation_probability,
        method_of_selection,
        elitism_size,
        quantity_of_crossing,
        quantity_of_generation,
    )
    if result_of_check:
        genetic_algoritm = GeneticAlgoritm(
            chromosome_size,
            population_size,
            crossing_probability,
            mutation_probability,
            method_of_selection,
            elitism_size,
            quantity_of_crossing,
            quantity_of_generation,
        )
        if genetic_algoritm.method_of_selection == 2:
            genetic_algoritm.set_tournament_size(tournament_size)
        return genetic_algoritm
    else:
        return False
