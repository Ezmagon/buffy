import random
from buffy.computer_vision import VisionForRobot

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
        pass
    def observe(self):
        eyes = VisionForRobot()
        print ("Eyes recognized", eyes.recognize_numbers())
        """
        Observe the pH
        :return: pH as float
        """
        return self.b.read_ph()
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
        def action():
            """
            Input: action parameters
            Do the action to influence
            :return: None
            """
            self.b.add_drip(ab)
        return action

    def at_goal(self):
        """
        Determine if goal pH is reached
        :return:
        """
        if self.observe() == round(self.g):
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
            action = self.evaluate()
            # Run the action (add acid or base)
            action()
            # Report to the user
            self.report()
        return "Goal achieved!"
