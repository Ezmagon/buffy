"""
Contains only graphing functions to be used throughout the project
"""
# Custom
from buffy.tools import generate_poly
# Builtin
import time
# Graphics
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from IPython import display
# Math
import numpy as np

def plot_robot_graphs(buffy):
    """
    Plots the behaviour of the buffer curve in "real" time
    :param buffy:
    :return:
    """
    data = buffy.read_mind()
    # Get the real polynomial for plotting
    poly = buffy.b.s.poly
    real_data = np.array([[x, np.polyval(poly, x)] for x in np.arange(0.6, -1.1, -0.02)])

    fig, ax = plt.subplots()
    ax.plot(real_data[:, 0], real_data[:, 1], c='C1')[0]
    margin = np.average(data[:, 0]) * 0.5
    if buffy.g < buffy.b.s.start:
        margin *= -1
    lim = (np.min(data[:, 0]) + margin, np.max(data[:, 0]) - margin)
    ax.set_xlim(lim[1], lim[0])
    x = []
    y = []
    ax.set_ylim(1, 14)
    ax.hlines([buffy.b.s.start, buffy.g], lim[1], lim[0])
    ax.text(lim[0], buffy.b.s.start, "Start", ha='left', va='center')
    ax.text(lim[0], buffy.g, "Goal", ha='left', va='center')
    plt.show(block=False)
    plt.pause(0.01)
    first = True
    for t, p in data:
        x.append(t)
        y.append(p)
        display.clear_output(wait=True)
        display.display(plt.gcf())
        ax.plot(x, y, marker='o', c='C0')
        if not first:
            poly_data = generate_poly(x, y, lim)
            ax.plot(poly_data[:, 0], poly_data[:, 1], c="C2")
        time.sleep(0.5)
        plt.draw()
        plt.pause(0.001)
        ax.lines.pop(-1)
        first = False
    poly_data = generate_poly(x, y, lim)
    ax.plot(poly_data[:, 0], poly_data[:, 1], c="C2", zorder=4)
    plt.show()