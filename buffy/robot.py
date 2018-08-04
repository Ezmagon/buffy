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
        :return: pH as float
        """
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
    def at_goal(self):
        """
        Determine if goal pH is reached
        :return:
        """
        if round(self.observe()) == round(self.g):
            return True
        else:
            return False
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
        while not self.at_goal():
            # Evaluate what to do
            ab = self.evaluate()
            # Run the action (add acid or base)
            self.action(ab)
            # Report to the user
            self.report()
        return "Goal achieved!"
