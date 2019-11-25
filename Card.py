#Card class is a blueprint of the Card object
# parent class or base class
class Card:

    # initializer to create the attributes of every class object (sometimes called instructor)
    def __init__(self, cost, name):
        self.cost = cost
        self.name = name
        #  attributes describes the object-argument parameter
        # give the Card a cost attribute
        # give the Card a name attribute

# behaviors-methods or functions
    def printCardInfo(self):
        print('The card costs: ' + str(self.cost))
        print('The card name: ' + self.name)
       