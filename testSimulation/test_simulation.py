from buffy.simulation import Simulation
import math

s = Simulation(pka = 7, c = 0.5, v = 1)

print(s.read_ph(0.3))