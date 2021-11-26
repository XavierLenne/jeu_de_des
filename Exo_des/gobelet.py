from des import Dice

class Goblet(Dice):
    def __init__(self):
        self.goblet=0
        self.goblet_list=0
    def goblet_pool(self):
        self.goblet_list=[0]
        self.goblet=int(input("Nombre de Dès: "))
        for i in range(self.goblet):
            i=Dice(self.goblet).get_dice_value()
            self.goblet_list.append(i)
        return self.goblet_list
    def get_goblet_value(self):
        for d in range(self.goblet):
            d=Dice
            self.goblet_list.append(d)
        return self.goblet_list
    def scoring(self):
        for d in range(1, len(self.goblet_list)):
            print(d)

device=Goblet()
device.goblet_pool()
# device.scoring()