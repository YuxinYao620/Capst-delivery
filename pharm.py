from Shop import Shop
class Pharm(Shop):
    pharmList = []
    def __init__(self,name,position,stock,volunteer):
        super().__init__(name, position,stock, volunteer)
        Pharm.pharmList.append(self)


