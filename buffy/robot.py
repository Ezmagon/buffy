#from buffy.computer_vision import VisionForRobot
import numpy as np
import matplotlib.pyplot as plt
from IPython import display
import time
import math

class Robot():
    """
    Main robot class
    Robot observes, evaluates and takes action
    Contains the buffer its holding and knows the goal pH value

    run() method integrates the class method in a loop to reach the goal pH of the internal buffer
    """
    def __init__(self, goal, buffer):
        self.g = goal
        self.b = buffer
        start_ph = self.b.ph
        self.mem = [[0, start_ph]] # "memory" of previous ph values and how many drops were added

    def read_mind(self):
        return np.array(self.mem)

    def observe(self):

        #eyes = VisionForRobot()
        #print ("Eyes recognized", eyes.recognize_numbers())
        """
        Observe the pH
        Has to observe several times because of noise
        note: will add noise later
        :return: pH as float
        """

        self.b.set_ph()
        return self.b.get_ph()

    def evaluate(self):
        """
        Evaluate whether to add acid or base
        Determine drip size
        :return: action function
        """
        if self.observe() > self.g:
            # Add acid to lower pH
            ab = 'acid'
        else:
            # Add base to increase pH
            ab = 'base'
        # Start with idk random number of drops
        # n_drops = random.randint(1,10) # use later
        #if len(self.mem) >= 5:
        #    data = self.read_mind()
        #    slope = abs(
        #        np.gradient(
        #            [data[-5],
        #             data[-1]]
        #        )[1][-1][0]
        #    )
        #    n_drops = self.determine_drops(slope)
        #else:
        n_drops = 4
        return ab, n_drops

    def action(self, ab, n_drops):
        """
        Input: action parameters
        Do the action to influence
        :return: None
        """
        for x in range(n_drops):
            self.b.add_drip(ab)

    def report(self):
        """
        Report internal status to user
        :return:
        """
        print(self.observe())

    def run(self):
        """
        Integrate robot methods
        :return:
        """
        while not within_range(self.observe(), self.g):
            # Evaluate what to do
            ab, n_drops = self.evaluate()
            # Run the action (add acid or base)
            self.action(ab, n_drops)
            # Observe the change
            new_ph = self.observe()
            if ab == "acid":
                #total_drops = self.mem[-1][0] - self.b.total_hc
                total_drops = self.b.total_hc
            elif ab == "base":
                #total_drops = self.mem[-1][0] + self.b.total_hc
                total_drops = self.b.total_hc
            # Record the change in memory plus the number of drops
            self.mem.append(
                [total_drops, new_ph]
            )
            # Report to the user
            #self.report()
        print ("Finished! pH = ", self.b.ph)
        return

    def plot_robot_graphs(self):
        # plt.plot(self.b.s.data[:, 0], self.b.s.data[:, 1])
        # plt.xlabel("Added Acid or Base")
        # plt.ylabel("pH")
        # plt.show(block=False)
        #

        data = self.read_mind()

        poly = self.b.s.poly

        real_data = np.array([[x, np.polyval(poly, x)] for x in np.arange(0.2, -1.0, -0.02)])

        # plt.ion()

        fig, ax = plt.subplots()
        ax.plot(real_data[:, 0], real_data[:, 1], c='C1')[0]
        lim = ax.get_xlim()
        ax.set_xlim(lim[1], lim[0])
        x = []
        y = []
        ax.hlines([self.b.s.start, self.g], lim[1], lim[0])
        plt.show(block=False)
        plt.pause(0.01)
        for t, p in data:
            x.append(t)
            y.append(p)
            display.clear_output(wait=True)
            display.display(plt.gcf())
            ax.plot(x, y, marker='o', c='C0')
            time.sleep(0.5)
            plt.draw()
            plt.pause(0.001)
        plt.show()



def within_range(a,b):
    """
    Check if a is within range of b
    :param a: float
    :param b: float
    :return: bool
    """
    acc = a*0.01
    lim = (a-acc, a+acc)
    return lim[0] < b < lim[1]