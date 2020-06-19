# from item import Item
# from volunteer import Volunteer
import priorityqueue
class Shop():
    #-30min
    def __init__(self,name,position,stock):
        self.name = name
        self.position = position
        # if isinstance(stock,list):
        #     self.stock = stock #dictionary /hash
        # else:
        #     raise TypeErro
        self.stock = []
        self.updateStock(stock[0],stock[1])
        # self.volunteer = []
        # self.neighbourShop
        # = neighbourShop

        self.priQ = priorityqueue.Queue(self)

    def updateStock(self,item,amount):
        self.stock.append([item,amount])
        return self.stock

    def getStock(self):
        return self.stock[0][1]
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

    # def initialVolunteer(self):
    #     list = []
    #     for i in Volunteer.volunList:
    #         dis = i.dis(self.position)
    #         if  dis< 2:
    #             list.append((i,dis))
    #     list.sort(2)
    # def arrangeVolun(self):
    #     fo


    # def checkStock(self,item,amount):
    #     if item in self.stock:
    #         if amount <= self.stock[item]:
    #             return 0 #request负责upadate数量
    #         elif amount > self.stock[item]:
    #             return self.stock[item]
    #     else:
    #         return -1

    def checkStock(self,ing):
        for i in self.stock:
            if i[0] == ing:
                return i[1]

        return 0

    def __str__(self):
        return str(self.name)
    def cost(self,request):
        pass                 #之后记得写 return cost value

    def __eq__(self, other):
        if isinstance(other,Shop):
            return self.name == other.name
        else:
            return False
    def addRequest(self,request,amount):
        self.priQ.addRequest(request,amount)


# a = "A"
# b = "B"
# s = Shop("name",(10,10.0),{"a":1,"b":2},[a,b],None)
# print(s.updateStock("a",2))
# print(s.updateStock("c",3))