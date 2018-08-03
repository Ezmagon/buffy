class Buffer():
    def __init__(self, ph_start):
        self.pH = ph_start

    def add_drip(self, base_or_acid, n_drips):
        if base_or_acid == "base":
            self.pH += 1*n_drips
        elif base_or_acid == "acid":
            self.pH -= 1*n_drips
        else:
            print("ERROR")

    def read_ph(self):
        return self.pH