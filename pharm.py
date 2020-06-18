from shop import Shop
class Pharm(Shop):
    pharmList = []
    def __init__(self,name,position,stock):
        super().__init__(name, position,stock)
        Pharm.pharmList.append(self)


