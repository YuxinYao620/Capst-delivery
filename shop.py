from Item import Item
class Shop():
    #-30min
    def __init__(self,name,position,stock,volunteer):
        self.name = name
        self.position = position
        if isinstance(stock,dict):
            self.stock = stock #dictionary /hash
        else:
            raise TypeError
        self.volunteer = volunteer
        # self.neighbourShop = neighbourShop


    def updateStock(self,item,amount):
        self.stock[item] = amount
        return self.stock

    # @property
    # def neighbourShop(self):
    #     return self.neighbourShop
    #
    # @neighbourShop.setter
    # def neighbourShop(self,shopList):
    #     for i in shopList:
    #         if i.name["type"] == self.name["type"]:
    #             if i.disShop(self.position) < 2:
    #                 self.neighbourShop.append(i)

    def get_volunteer(self,volunList):
        for i in volunList:
            if i.disShop(self.position) < 2:
                self.volunteer.append(i)

    def checkStock(self,item,amount):
        if item in self.stock:
            if amount <= self.stock[item]:
                return 0 #request负责upadate数量
            elif amount > self.stock[item]:
                return self.stock[item]
        else:
            return -1

    def cost(self,request):
        pass                 #之后记得写 return cost value




a = "A"
b = "B"
s = Shop("name",(10,10.0),{"a":1,"b":2},[a,b],None)
print(s.updateStock("a",2))
print(s.updateStock("c",3))