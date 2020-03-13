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


def show_chart(
    best_chromosome_list, genetic_algoritm,
):
    from project2.control.functions import calculate_fitness
    import math

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    x = np.arange(-3.1, 12.1, 0.01)
    y = np.arange(4.1, 5.8, 0.01)
    X, Y = np.meshgrid(x, y)
    Z = 21.5 + X * np.sin(4 * math.pi * X) + Y * np.sin(20 * math.pi * Y)
    bin_x, bin_y = (
        best_chromosome_list[index].genetic_code[
            : int(len(best_chromosome_list[index].genetic_code) / 2)
        ],
        best_chromosome_list[index].genetic_code[
            int(len(best_chromosome_list[index].genetic_code) / 2) :
        ],
    )
    real_x = genetic_algoritm.get_conversion_from_binary_to_real_x(bin_x)
    real_y = genetic_algoritm.get_conversion_from_binary_to_real_y(bin_y)
    zdata = calculate_fitness(real_x, real_y)
    xdata = real_x
    ydata = real_y

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, alpha=0.2)

    sc.append(ax.scatter(xdata, ydata, zdata, c="r", marker="o"))

    def animate(i):
        global sc
        global index
        real_y = 0
        real_x = 0
        bin_x = 0
        bin_y = 0
        zdata = 0
        if index < len(best_chromosome_list):
            bin_x, bin_y = (
                best_chromosome_list[index].genetic_code[
                    : int(len(best_chromosome_list[index].genetic_code) / 2)
                ],
                best_chromosome_list[index].genetic_code[
                    int(len(best_chromosome_list[index].genetic_code) / 2) :
                ],
            )
            real_x = genetic_algoritm.get_conversion_from_binary_to_real_x(bin_x)
            real_y = genetic_algoritm.get_conversion_from_binary_to_real_y(bin_y)
            zdata = calculate_fitness(real_x, real_y)
            print(zdata)
            for s in sc:
                s.remove()

            sc = []

            sc.append(ax.scatter(real_x, real_y, zdata, c="r", marker="o"))
            index += 1

        return sc

    finish = int(len(best_chromosome_list))

    ani = animation.FuncAnimation(fig, animate, interval=2000)
    plt.show()


def show_chart2(best_chromosome_list, quantity_of_generation):
    from matplotlib.animation import FuncAnimation
    import matplotlib.pyplot as plt

    fitness_list = []
    generation_list = []

    for bestChromosome in best_chromosome_list:
        fitness_list.append(bestChromosome.fitness)
        generation_list.append(bestChromosome.generation)

    fig = plt.figure(1)
    plt.xlim(0, quantity_of_generation)
    plt.ylim(0, 40)
    (graph,) = plt.plot([], [], lw=3)
    plt.grid(
        axis="both",
        which="major",
        color=[166 / 255, 166 / 255, 166 / 255],
        linestyle="-",
        linewidth=2,
    )
    plt.minorticks_on()
    plt.grid(
        axis="both",
        which="minor",
        color=[166 / 255, 166 / 255, 166 / 255],
        linestyle=":",
        linewidth=2,
    )
    plt.xlabel("Generation")
    plt.ylabel("Fitness")

    def animate(i):
        graph.set_data(generation_list[: i + 1], fitness_list[: i + 1])
        return graph

    ani = FuncAnimation(fig, animate, interval=100)
    plt.show()
