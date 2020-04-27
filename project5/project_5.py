import os 
import numpy as np
from project5.model.NeuralNetwork import NeuralNetwork
from project5.control.functions import *
import random
import matplotlib.pyplot as plt
import copy
from project5.view.result_display import show_chart2


def run_neural_network():
    os.chdir(r"/home/lucas/College/IA/AI-codes/project5")

    neural_net : NeuralNetwork = NeuralNetwork(
        stop_type = 0,
        max_error = 0.05,
        learning_rate = 0.01,
        max_cycles= 10,
        actual_cycle = 0,
    )

    # TRAINING START
    loaded_txt_entries = np.loadtxt('entriesTest.txt')
    loaded_txt_targets = np.loadtxt('targets.txt')

    (samples_size,entries_size) = np.shape(loaded_txt_entries)
    (classes_size,targets_size) = np.shape(loaded_txt_targets)

    



    v = intiate_syntactic_weights_matrix(entries_size,classes_size)
    v0 = intiate_bias(classes_size)
 
    

    yin = np.zeros((classes_size,1))
    y = np.zeros((classes_size,1))

    actual_error = 10
    actual_cycle = 1
    threshold = 0.5
    vetor1 = []
    vetor2 = []

    if neural_net.stop_type == 0:

        while(actual_error > neural_net.max_error ):
            actual_error = 0
            for i in range(samples_size):
                #Calculate pure output

                yin = calculate_pure_output(i,loaded_txt_entries,classes_size,entries_size,v,v0)
                
                #Calculate liquid innput
                y = calculate_output(classes_size,threshold,yin)


                #calculate new error
                
                actual_error = atualize_error(classes_size,actual_error,loaded_txt_targets,i,y)
                
                # Atualizing syntactic weights
                v = atualize_syntactic_weights(v,entries_size,classes_size,neural_net.learning_rate,loaded_txt_targets,loaded_txt_entries,i,y)

                #Atualizing bias
                v0 = atualize_bias(v0,classes_size,loaded_txt_targets,neural_net.learning_rate,y,i)

                
                
        
            vetor1.append(actual_cycle)
            vetor2.append(actual_error)
            actual_cycle += 1
        #END TRAINING


    if neural_net.stop_type == 1:
        
        while(actual_cycle < neural_net.max_cycles ):
            actual_error = 0
            for i in range(samples_size):
                #Calculate pure output

                yin = calculate_pure_output(i,loaded_txt_entries,classes_size,entries_size,v,v0)
                
                #Calculate liquid innput
                y = calculate_output(classes_size,threshold,yin)


                #calculate new error
                
                actual_error = atualize_error(classes_size,actual_error,loaded_txt_targets,i,y)
                
                # Atualizing syntactic weights
                v = atualize_syntactic_weights(v,entries_size,classes_size,neural_net.learning_rate,loaded_txt_targets,loaded_txt_entries,i,y)

                #Atualizing bias
                v0 = atualize_bias(v0,classes_size,loaded_txt_targets,neural_net.learning_rate,y,i)

                
                
        
            vetor1.append(actual_cycle)
            vetor2.append(actual_error)
            actual_cycle += 1
        #END TRAINING

    show_chart2(vetor2,vetor1)
    plt.scatter(vetor1,vetor2,color='blue')
    plt.xlabel("Ciclos")
    plt.ylabel("Erro")
    plt.show()


    # TESTING THE TRAINING
    xteste = loaded_txt_entries[3,:]
    
    for m2 in range(classes_size):
        total_sum = 0
        for n2 in range(entries_size):
            total_sum = total_sum + xteste[n2] * v[n2][m2]
            yin[m2] = total_sum + v0[m2]   

    print(yin)
    for j in range(classes_size):
        if(yin[j] >= threshold):
            y[j] = 1.0
        else:
            y[j] = 0.0
    print(y)
    
    
     
   

    
     


    




    # SOLUCAO SEM USAR FUNCAO
    '''
    while(actual_error > neural_net.max_error):
        actual_error = 0
        for i in range(samples_size):
            xaux = loaded_txt_entries[i,:]
            for m in range(classes_size):
                total_sum = 0
                for n in range(entries_size):
                    total_sum = total_sum + xaux[n]*v[n][m]
                yin[m] = total_sum + v0[m]
            for j in range(classes_size):
                if yin[j] >= threshold:
                    y[j] = 1.0

                else:
                    y[j] = 0.0

            for j in range(classes_size):
                actual_error = actual_error + 0.5*((loaded_txt_targets[j][i] - y[j])**2)

            lastV = v

            for m in range(entries_size):
                for n in range(classes_size):
                    v[m][n] = lastV[m][n] + neural_net.learning_rate *(loaded_txt_targets[n][i]-y[n]) * xaux[m]
            

            lastV0 = v0

            for j  in range(classes_size):
                
                v0[j] = lastV0[j]+neural_net.learning_rate*(loaded_txt_targets[j][i] - y[j])
                
            
            

        vetor1.append(actual_cycle)
        vetor2.append(actual_error)
        actual_cycle = actual_cycle + 1
    '''
    #FIM DA SOLUCAO SEM FUNCAO