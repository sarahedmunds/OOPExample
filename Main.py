from Card import Card
from Minion import Minion

def main():
    # create the townCrier Card
    # cost = 1 and name = 'Town Crier'
    # instantiate an object called townCrier
    # creating an instance of the class
    townCrier = Minion(1, 'Town Crier', 1, 2)
    
    # Create an instance of the class called redbandwasp
    # Attribtues cost = 2, name = Redband Wasp
    redbandWasp = Minion(2, 'Redband Wasp', 1, 3)

    # Name = war path cost = 2
    warPath = Card(2, 'Warpath')
    # Show the player the details of the Card

    townCrier.printCardInfo()
    townCrier.printMinionInfo()
    
    redbandWasp.printCardInfo()
    warPath.printCardInfo()

if __name__=="__main__":
    main()