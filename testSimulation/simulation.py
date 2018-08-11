import time


class Simulation (object):
    def __init__(self, ph_start):
        self.pH = ph_start

    def add_drip(self, drip):
        if drip.baseOrAcid == "base":
            self.pH += drip.size # make more chemical
        elif drip.baseOrAcid == "acid":
            self.pH -= drip.size
        else:
            print("ERROR")
        time.sleep(0.5)

