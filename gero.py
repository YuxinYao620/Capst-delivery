from shop import Shop

class Gerocery(Shop):
    geroList = []
    def __init__(self,name,position,stock):
        super().__init__(name,position,stock)
        Gerocery.geroList.append(self)
