import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import ctypes

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def show_chart(bestChromosome, geneticAlgoritm):
    from project1.control.functions import calculate_fitness
    import math
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

  
    x = np.arange(-3.1, 12.1, 0.01)
    y = np.arange(4.1, 5.8, 0.01)
    X, Y = np.meshgrid(x, y)
    Z = 21.5 + X * np.sin(4*math.pi*X) + Y * np.sin(20*math.pi*Y)


    binX, binY = bestChromosome.geneticCode[:int(len(bestChromosome.geneticCode) / 2)], bestChromosome.geneticCode[int(len(bestChromosome.geneticCode) / 2):]
    realX = geneticAlgoritm.getConvertionFromBinaryToRealX(binX)
    realY = geneticAlgoritm.getConvertionFromBinaryToRealY(binY)
    zdata = calculate_fitness(realX, realY)
    xdata = realX
    ydata = realY

    ax.set_xlabel('X ')
    ax.set_ylabel('Y ')
    ax.set_zlabel('Z ')
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, alpha=0.2)

    ax.scatter(xdata, ydata, zdata, c='r', marker='o')
    plt.show()
    Mbox('Resultado', "CURRENT BEST CHRMOSSOME: " + bestChromosome.geneticCode + 
            "\nGeneration: " + str(bestChromosome.generation) + 
            "\nFitness: " + str(bestChromosome.fitness) , 0)
