from project3.project_3 import run_genetic_algoritm_2, run_teste
from project2.project_2 import run_genetic_algoritm_1, test
from project1.project_1 import run_genetic_algoritm
from project5.project_5 import run_neural_network
from project6.project_6 import run_neural_network2
from project7.project_7 import run_neural_network_7

#  Algoritm_option = input("Select the project number: ")

algoritm_option = 7
if int(algoritm_option) == 1:
    run_genetic_algoritm()
elif int(algoritm_option) == 2:
    # test()
    run_genetic_algoritm_1()
elif int(algoritm_option) == 3:
    run_genetic_algoritm_2()


elif int(algoritm_option) == 5:
    run_neural_network()
elif int(algoritm_option) == 6:
    run_neural_network2()

elif int(algoritm_option) == 7:
    run_neural_network_7()