from project1.control.functions import get_values_from_user
from project1.project_1 import run_genetic_algoritm

algoritmOption = input("Select the project number: ")
if int(algoritmOption) == 1:
    run_genetic_algoritm()
