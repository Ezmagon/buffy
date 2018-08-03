class Robot():
    def __init__(self, goal):
        self.goal = goal
        pass
    def observe(self):
        """
        Observe the pH
        :return: pH as float
        """
        pass
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
