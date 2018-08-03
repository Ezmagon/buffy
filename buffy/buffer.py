class Buffer():
    def __init__(self, ph_start):
        self.pH = ph_start

    def add_drip(self, base_or_acid):
        if base_or_acid == "base":
            self.pH += 1
        elif base_or_acid == "acid":
            self.pH -= 1
        else:
            print("ERROR")

    def read_ph(self):
        return self.pH