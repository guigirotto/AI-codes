from project3.project_3 import run_genetic_algoritm_2,run_teste
from project2.project_2 import run_genetic_algoritm_1, test
from project1.project_1 import run_genetic_algoritm

#  Algoritm_option = input("Select the project number: ")
algoritm_option = 3
if int(algoritm_option) == 1:
    run_genetic_algoritm()
elif int(algoritm_option) == 2:
    # test()
    run_genetic_algoritm_1()
elif int(algoritm_option) == 3:
    run_genetic_algoritm_2()
