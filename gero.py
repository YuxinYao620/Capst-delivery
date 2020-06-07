from Shop import Shop

class Gerocery(Shop):
    geroList = []
    def __init__(self,name,position,stock,volunteer):
        super().__init__(name,position,stock,volunteer)
        Gerocery.geroList.append(self)