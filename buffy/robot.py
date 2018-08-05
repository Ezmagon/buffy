#from buffy.computer_vision import VisionForRobot
import numpy as np
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
        #for x in range(n_drops):
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
                total_drops = self.mem[-1][0] + n_drops
            elif ab == "base":
                total_drops = self.mem[-1][0] - n_drops
            # Record the change in memory plus the number of drops
            self.mem.append(
                [total_drops, new_ph]
            )
            # Report to the user
            #self.report()
        return

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