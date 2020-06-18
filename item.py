# from pharm import Pharm
# from gero import Gerocery
from requestqueue import requestQ
class Item():
    def __init__(self,name,type):
        self.name = name #check string
        self.type = type #check T or F
        self.requestqueue = requestQ(self)

    def __eq__(self,other):
        if not isinstance(other,Item):
            return False
        return (self.name) == (other.name)

    def isMedi(self):
        return type

    # @property
    # def name(self):
    #     return self.name
    #
    # @name.setter
    # def name(self,name):
    #     self.name = name

    def addRequest(self):
        self.requestqueue.addR(self)


    # def getAmount(self):
    #     return self.amount()