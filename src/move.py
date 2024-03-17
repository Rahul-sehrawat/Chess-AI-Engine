from const import *

class Move:
    
    def __init__(self, initial, final):
        self.initial = initial # Starting position(square)
        self.final = final # Ending position(square)

    def __str__(self):
        return str(self.initial) + ', ' + str(self.final)

    def __eq__(self, other):
        return self.initial == other.initial and self.final == other.final