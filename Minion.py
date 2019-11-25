# this class needs to inherit the attributes and behaviors of the Card class
# a Minion object is a Card
# child class or derived class
from Card import Card

class Minion(Card):
    # attribute cost and name
    # inherits cost and name from the parent class Card
    def __init__(self, cost, name, damage, life):
        Card.__init__(self, cost, name)
        # assign parameters to the object
        self.damage = damage
        self.life = life
    
    def printMinionInfo(self):
        print('The card costs: ' + str(self.cost))
        print('The card name: ' + self.name)
        print('damage: ' + str(self.damage))
        print('life: ' + str(self.life))