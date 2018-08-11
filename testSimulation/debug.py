import importlib
from buffy.robot import Robot
from buffy.buffer import Buffer
from buffy.simulation import Simulation
from sys import argv
import matplotlib.pyplot as plt
import time
from IPython import display
import numpy as np


def debug(*argv):
    goal = float(argv[0])

    # Initialize the simulation
    s = Simulation(pka=7, c=0.5, v=1, start=4)
    # Initialize the buffer, using the simulation
    b = Buffer(s, 4)

    # Create buffy
    buffy = Robot(goal, b)
    # Let buffy do its thing
    buffy.run()

    return buffy


buffy = debug(9)

data = buffy.read_mind()

poly = buffy.b.s.poly

real_data = np.array([[x,np.polyval(poly, x)] for x in np.arange(0.2, -1.2, -0.02)])

plt.ion()

fig, ax = plt.subplots()
ax.plot(real_data[:,0],real_data[:,1], c='C1')
lim = ax.get_xlim()
ax.set_xlim(lim[1], lim[0])
x = []
y = []
ax.set_title = "pH over time"
ax.set_xlabel = "H+ added"
ax.set_ylabel = "pH"
for t, p in data[::3000]:
    x.append(t)
    y.append(p)
    display.clear_output(wait=True)
    display.display(plt.gcf())
    ax.plot(x, y, marker='o', c='C0')
    time.sleep(0.5)
plt.close()
plt.show()