import math

class Buffer():
    def __init__(self, s, pipet_size=math.pow(10,-6)):
        """
        The buffer contains a buffer solution.
        Bases or acids can be added to find new pH values
        :param pKa:
        :param Amin:
        :param HA:
        """
        self.s = s
        #self.pKa = pKa
        #self.Amin = Amin
        #self.HA = HA
        self.pipet_size = pipet_size
        self.total_hc = 0
        self.set_ph()

    def add_drip(self, base_or_acid):
        """
        Changes the pH based on a drip of base or acid
        :param base_or_acid:
        :return:
        """
        if base_or_acid == "base":
            self.total_hc -= self.pipet_size
        elif base_or_acid == "acid":
            self.total_hc += self.pipet_size
        else:
            print("ERROR")
        self.set_ph()

    #def calculate_pH(self):
    #    """
    #    :return: pKa + log10(Amin/HA)
    #    """
    #    return math.pow(self.Amin, 3)
    #    # return self.pKa + math.log10(self.Amin / self.HA)

    def set_ph(self):
        """
        Read the pH value
        :return: pH value
        """
        self.ph = self.s.read_ph(self.total_hc)