from simulation import Simulation
from drip import Drip
from random import *


def test(pH_goal = 10):
    s = Simulation(3)
    out = []
    t = 0
    out.append((t, s.pH))
    while round(s.pH) != pH_goal:

        size = randint(1, 10)
        size /= 10
        size = round(size, 1)
        if s.pH < pH_goal:
            bOrA = "base"
            t += size
        else:
            bOrA = "acid"
            t -= size
        d = Drip(size, bOrA)
        s.add_drip(d)
        out.append((t, s.pH))
        print(s.pH)
    #print(s.pH)
    # This always happens
    #if s.pH == pH_goal:
    print ("Goal Achieved!")
    return out

