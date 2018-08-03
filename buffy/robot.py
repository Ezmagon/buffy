import Interface

class Robot():
    def __init__(self, goal, buffer):
        self.g = goal
        self.b = buffer
        pass
    def observe(self):
        """
        Observe the pH
        :return: pH as float
        """
        return b.read_ph()
    def evaluate(self):
        """
        Input: current pH
        :return: action parameters (acid/base, n drops)
        """
        pass
    def action(self):
        """
        Input: action parameters
        Do the action to influence
        :return: None
        """
        pass
    def run(self):
        """
        Integrate robot methods
        :return:
        """
        while