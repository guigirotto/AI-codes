import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import ctypes
import matplotlib.animation as animation




sc = []
index = 0

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def show_chart(bestChromossomeList, geneticAlgoritm,):
    from project1.control.functions import calculate_fitness
    import math
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    #for bestChromosome in bestChromossomeList:
     #   print(
      #          "CURRENT BEST CHRMOSSOME: " + bestChromosome.geneticCode + 
       #         "\nGeneration: " + str(bestChromosome.generation) + 
        #        "\nFitness: " + str(bestChromosome.fitness) 
        #)

  
    x = np.arange(-3.1, 12.1, 0.01)
    y = np.arange(4.1, 5.8, 0.01)
    X, Y = np.meshgrid(x, y)
    Z = 21.5 + X * np.sin(4*math.pi*X) + Y * np.sin(20*math.pi*Y)
    #print(bestChromossomeList[0].geneticCode)
    binX, binY = bestChromossomeList[index].geneticCode[:int(len(bestChromossomeList[index].geneticCode) / 2)], bestChromossomeList[index].geneticCode[int(len(bestChromossomeList[index].geneticCode) / 2):]
    realX = geneticAlgoritm.getConvertionFromBinaryToRealX(binX)
    realY = geneticAlgoritm.getConvertionFromBinaryToRealY(binY)
    zdata =(calculate_fitness(realX, realY))
    xdata =(realX)
    ydata =(realY)
    

    

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, alpha=0.2)
    
    sc.append(ax.scatter(xdata, ydata, zdata, c='r', marker='o'))
    
    
    def animate(i):
       global sc
       global index
       realY = 0
       realX = 0
       binX = 0
       binY = 0
       zdata = 0
       if index < len(bestChromossomeList):
           binX, binY = bestChromossomeList[index].geneticCode[:int(len(bestChromossomeList[index].geneticCode) / 2)], bestChromossomeList[index].geneticCode[int(len(bestChromossomeList[index].geneticCode) / 2):]
           realX = geneticAlgoritm.getConvertionFromBinaryToRealX(binX)
           realY = geneticAlgoritm.getConvertionFromBinaryToRealY(binY)
           zdata =(calculate_fitness(realX, realY))
           print(zdata)
           for s in sc:
                s.remove() 
           
           sc=[]
           
           sc.append(ax.scatter(realX, realY, zdata, c='r', marker='o'))
           index +=1
       
       
       return sc
           

      
    
    finish = int(len(bestChromossomeList))
       
    
    ani = animation.FuncAnimation(fig, animate, interval=5000)
    plt.show()
    
    
    #Mbox('Resultado', "CURRENT BEST CHRMOSSOME: " + bestChromosome.geneticCode + 
            #"\nGeneration: " + str(bestChromosome.generation) + 
            #"\nFitness: " + str(bestChromosome.fitness) , 0)
    

