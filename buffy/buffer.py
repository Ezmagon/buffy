# Custom
from buffy.simulation import Simulation
# Builtin
import math
import random

class Buffer():
    def __init__(self, sim = True):
        """
        The Buffer class contains an implementation for the buffer solution.
        Interacts with the underlying implementation for the buffer
        """
        if sim:
            # Initialize the simulation with a random pka between 4 and 9
            # Random concentration of acid and conjugated base between 0.2 M and 1.0 M
            # Random buffer volume between 0.2 L and 5 L
            self.s = Simulation(
                pka = random.randint(4, 9),
                c   = random.uniform(0.2, 1.0),
                v   = random.uniform(0.2, 5)
            )
            self.read_ph = self.read_ph_sim
        else:
            # Initialize real buffer, not implemented yet
            raise NotImplementedError("Real buffer is not implemented yet")
            self.read_ph = self.read_ph_real

        # Initialize the total acid added and read the starting ph from the buffer
        self.total_hc = 0

    def read_ph_sim(self):
        """
        Read the pH from a simulated buffer
        :return: Real pH with added noise
        """
        # Read the pH from the simulated buffer
        real_ph = self.s.read_ph()
        # Add some noise
        return real_ph + random.uniform(-0.2, 0.2)

    def read_ph_real(self):
        """
        Read pH from the real buffer using computer vision
        :return: Real pH
        """
        raise NotImplementedError()

    def add_drop_sim(self, ab, n):
        """
        Changes the pH based on a drip of base or acid
        :param ab: 'acid' or 'base'
        :param n: "number of drops to add
        :return:
        """
        self.s.add_drop(ab, n)

    def add_drop_real(self):
        raise NotImplementedError()