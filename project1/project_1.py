#
# Artificial intelligence - Project 1
# Computer Engeneering - Semester 9
# Genetic Algoritm - Using Roullete or Tornment method
# Date February 09, 2020
#

from project1.control.functions import get_values_from_user


def run_genetic_algoritm():
    inputResult = get_values_from_user()
    if not inputResult:
        print('Ops, something went wrong')
    else:
        print('Success !')
