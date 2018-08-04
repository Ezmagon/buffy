import math
import numpy as np
import random

class Simulation():
    """
    Buffer has two linear domains and a buffering domain in the middle
    At the linear domains, buffer concentrations approach zero so cannot be computed
    """
    def __init__(self, pka, c, v, h = math.pow(10, -5)):
        """
        Initialze the buffer with its pka, ph will also be the pka
        initial buffer concentration is also required
        self.data contains buffer data
        """
        # Initialize variables
        self.ph = pka
        self.pka = pka
        self.c = c #Keep concentration for resetting
        self.v = v #volume
        self.h = h #number of H+ moles to add
        self.data = [] # initialize data, will be converted to numpy by setup()

        # Run the simulation to get buffer data
        self.setup()
    def read_ph(self, total_hc, n = 0):
        """
        Read the "real" pH from the simulation, but add some random noise
        :param total_hc: total added acid/base
        :return: "real" pH
        """
        return np.polyval(self.poly, total_hc)
        """ Veel meer werk dan ik dacht...
        if total_hc < 0: # ph increases
            noisy_ph = real_ph - 0.01*n*real_ph
        else:
            noisy_ph = real_ph + 0.01 * n * real_ph
        return noisy_ph
        """

    def reset(self):
        """
        reset the internal buffer
        :return:
        """
        self.ph = self.pka
        self.a = self.c #acid (HA) molar
        self.b = self.c #base (A-) molar
        self.total_hc = 0

    def rec_hc(self, hc):
        """
        Record total hc added
        :param hc: H+ concentration
        :return:
        """
        self.total_hc += hc

    def buffer(self, hc):
        """
        Compute the pH of the buffer
        Subtract the H+ conentration from the base (because it reacts)
        And add to the acid (because it is created)
        :param h: H+ concentration
        """
        # Record added hc
        self.rec_hc(hc)

        self.b -= hc
        self.a += hc
        # Use buffer equation to calculate new ph
        # https://en.wikipedia.org/wiki/Henderson%E2%80%93Hasselbalch_equation
        try:
            self.ph = self.pka + math.log((self.b / self.a), 10)
        except ValueError as e:
            print(self.a, self.b)

    def linear(self, hc):
        """
        input: H+ FINAL concentration added

        Compute the linear domain
        Calculate total number of moles H+
        Add the required amount
        Calculate back to concentration
        :return:
        """
        # Record added hc
        self.rec_hc(hc)
        # Calculate current H+ concentration
        current_hc = 1/math.pow(10, self.ph)
        # Calculate the new concentration
        new_hc = current_hc + hc
        # Fail safe for if new_hc < 0
        if new_hc < 0:
            new_hc = math.pow(10, -14)
        elif new_hc > 0.1:
            new_hc = 0.1
        # Convert to pH by -log10(H+)
        self.ph = math.log10(new_hc) * -1

    def rec_data(self):
        """
        Record current state
        :return:
        """
        self.data.append(
            (self.total_hc, self.ph)
        )
    def setup(self):
        """
        Compute buffer pH for both sides, starting at the pKa
        :return:
        """
        hc = self.h/self.v
        # First reset the buffer
        self.reset()
        # Then calculate the first half of the buffer regime
        # base is added, acid will react away
        # Do this until acid is almost gone
        # hc will be -hc because base is added
        while self.a > self.h*2:
            self.buffer(-1*hc)
            # Record new ph and H+ added
            self.rec_data()
        # Now we are in the linear regime,
        # while the pH is lower than 14, add base
        while self.ph < 14:
            self.linear(-1*hc)
            # Record state
            self.rec_data()
        # Now reset the buffer
        self.reset()
        # Not working yet
        # Start over, but add acid
        # Do this while the concentration of base is reasonable
        while self.b > self.h*2:
            self.buffer(hc)
            # Record state
            self.rec_data()
        # Now add more acid until the ph reaches 1
        while self.ph > 1:
            self.linear(hc)
            # Record data
            self.rec_data()
        # self.data now contains all the data points
        # convert into a numpy array and sort by hc added
        self.data = np.array(sorted(self.data, key = lambda x: x[1]))
        # Fit a polynomial to the data
        self.poly = np.polyfit(self.data[:,0], self.data[:,1], deg = 3)