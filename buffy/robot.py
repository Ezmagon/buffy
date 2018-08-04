#from buffy.computer_vision import VisionForRobot


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
    def observe(self):

        #eyes = VisionForRobot()
        #print ("Eyes recognized", eyes.recognize_numbers())
        """
        Observe the pH
        Has to observe several times because of noise
        :return: pH as float
        """
        n = 10 # noise
        prev_ph = self.b.ph
        self.b.set_ph(n)
        n -= 1
        obs_ph = self.b.ph
        while not within_range(obs_ph, prev_ph):
            prev_ph = obs_ph
            self.b.set_ph(n)
            n -= 1
            obs_ph = self.b.ph
        print("pH {:.2f} within range!".format(obs_ph))
        return self.b.ph
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

        return ab
    def action(self, ab):
        """
        Input: action parameters
        Do the action to influence
        :return: None
        """
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
            ab = self.evaluate()
            # Run the action (add acid or base)
            self.action(ab)
            # Report to the user
            #self.report()
        return "Goal achieved!"

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