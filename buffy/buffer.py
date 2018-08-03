import math

class Buffer():
    def __init__(self, pKa=0, Amin=-1, HA=1, pipet_size=0.1):
        """
        :param pKa:
        :param Amin:
        :param HA:
        """
        self.pKa = pKa
        self.Amin = Amin
        self.HA = HA
        self.pipet_size = pipet_size

    def add_drip(self, base_or_acid):
        """
        Changes the pH based on a drip of base or acid
        :param base_or_acid:
        :return:
        """
        if base_or_acid == "base":
            self.Amin += self.pipet_size
        elif base_or_acid == "acid":
            self.HA += self.pipet_size
        else:
            print("ERROR")

    def calculate_pH(self):
        """
        :return: pKa + log10(Amin/HA)
        """
        return math.pow(self.Amin, 3)
        # return self.pKa + math.log10(self.Amin / self.HA)

    def read_ph(self):
        """
        Read the pH value
        :return: pH value
        """
        return self.calculate_pH()