

def intiate_syntactic_weights_matrix(entries_size, classes_size):
    import random
    v = [ [ random.uniform(-0.1,0.1) for i in range(classes_size) ] for j in range(entries_size) ] 
    return v

def intiate_bias(classes_size):
    import random
    v0 = [ random.uniform(-0.1,0.1) for i in range(classes_size)]
    return v0

def calculate_pure_output(i,loaded_txt_entries,classes_size,entries_size,v,v0):
    import numpy as np
    yin = np.zeros((classes_size,1))
    
    xaux = loaded_txt_entries[i,:]
    for m in range(classes_size):
        total_sum = 0
        for n in range(entries_size):
            total_sum = total_sum + xaux[n]*v[n][m]
        yin[m] = total_sum + v0[m]
    
    return yin

def calculate_output(classes_size,threshold,yin):
    import numpy as np
    y = np.zeros((classes_size,1))
    for j in range(classes_size):
         if yin[j] >= threshold:
            y[j] = 1.0

         else:
            y[j] = 0.0
    return y

def atualize_error(classes_size,actual_error,loaded_txt_targets,i,y):
    for j in range(classes_size):
        actual_error = actual_error + 0.5*((loaded_txt_targets[j][i] - y[j])**2)
    
    return actual_error
    

def atualize_syntactic_weights(lastV,entries_size,classes_size,learning_rate,loaded_txt_targets,loaded_txt_entries,i,y):
    import numpy as np
    v = lastV

    xaux = loaded_txt_entries[i,:]
    for m in range(entries_size):
        for n in range(classes_size):
            v[m][n] = lastV[m][n] + learning_rate *(loaded_txt_targets[n][i]-y[n]) * xaux[m]

    return v

def atualize_bias(lastV0,classes_size,loaded_txt_targets,learning_rate,y,i):
    import numpy as np
    v0 = lastV0
    
    for j in range(classes_size):
        v0[j] = lastV0[j]+learning_rate*(loaded_txt_targets[j][i] - y[j])
    
    return v0
