import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def show_chart(geneticCode, geneticAlgoritm):
    from project1.control.functions import calculate_fitness
    import math
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    xline = np.linspace(0, 30, 100)
    yline = np.linspace(0, 30, 100)
    zline = 21.5 + xline*np.sin(4*math.pi*xline) + yline*np.sin(20*math.pi*yline)


    '''for i in range(1000):
        for j in range(1000):
            result = calculate_fitness(xline[i], yline[i])
            zline.append(result)
    '''

    ax.plot3D(xline, yline, zline)
    binX, binY = geneticCode[:int(len(geneticCode) / 2)], geneticCode[int(len(geneticCode) / 2):]
    realX = geneticAlgoritm.getConvertionFromBinaryToRealX(binX)
    realY = geneticAlgoritm.getConvertionFromBinaryToRealY(binY)
    zdata = calculate_fitness(realX, realY)
    xdata = realX
    ydata = realY

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    ax.scatter3D(xdata, ydata, zdata, c='r', marker='o')
    plt.show()
