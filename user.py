# from shop import Shop
from gero import Gerocery
from pharm import Pharm
from request import Request
import time
class User():
    def __init__(self,name,age,address,position,disease):
        self.name = name
        self.position = position
        self.age = age
        self.address = address
        self.disease = disease
        self.healthRisk = 100
        self.calRisk()
        self.neiGe = []
        self.neiPh = []
        self.nearestPharm()
        self.request = []

    def __getDistance(self,shop):
        return ((self.position[0] - shop.position[0])**2 + ((self.position[1] - shop.position[1]))**2)

    def nearestGero(self):
        for g in Gerocery.geroList:  # 算经纬度 <2
            dis = self.__getDistance(g)
            if dis < 2:
                self.neiGe.append([g,dis])
        sorted(self.neiGe, key = lambda shop:shop[1])
        return self.neiGe

    def nearestPharm(self):
        result = []
        for p in Pharm.pharmList:  # 算经纬度 <2
            dis = self.__getDistance(p)
            if dis < 120:
                result.append([p,dis])

        sorted(result, key=lambda shop: shop[1])
        self.neiPh = result

    def calRisk(self):
        for i in self.disease:
            self.healthRisk -= 5
        if self.age >= 65:
            self.healthRisk -= 5

    def getDis(self,shop):
        for a in self.neiPh:
            if a == shop:
                return a[1]

    def sendRequest(self,item,amount):
        self.request.append(Request(self,item,amount))
