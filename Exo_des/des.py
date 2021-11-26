import random

class Dice:
    def __init__(self, dice):
        self.dice=0
    
    @property
    def dice(self):
        return self._dice
    @dice.setter
    def dice(self, dice):
        self._dice=dice
    def get_dice_value(self):
        d =random.randint(1, 6)
        return d
    def throw_dice(self):
        return self.dice()