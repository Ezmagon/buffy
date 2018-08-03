from simulation import Simulation
from drip import Drip
from random import *

pH_goal = 10
s = Simulation(3)
while s.pH != pH_goal:
    print(s.pH)
    size = randint(1, 10)
    size /= 10
    size = round(size, 1)
    if s.pH < pH_goal:
        bOrA = "base"
    else:
        bOrA = "acid"
    d = Drip(size, bOrA)
    s.add_drip(d)
print(s.pH)
if s.pH == pH_goal:
    print ("Goal Achieved!")
