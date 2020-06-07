from Shop import Shop
from gero import Gerocery
from pharm import Pharm
class User():
    def __init__(self,name,age,adress,position,disease):
        self.name = name
        self.position = position
        self.age = age
        self.address = adress
        self.disease = disease
        self.vulunable = 0
        self.neiGe = []

    def __getDistance(self,shop):
        return (((self.position()[0] - shop.position()[0])**2) + ((self.position()[1] - shop.position()[1])**2))

    def nearestGero(self):
        for g in Gerocery.geroList:  # 算经纬度 <2
            dis = self.__getDistance(g)
            if dis < 2:
                self.neiGe.append({g,dis})

    def nearestPharm(self):
        for p in Pharm.pharmList:  # 算经纬度 <2
            dis = self.__getDistance(p)
            if dis < 2:
                self.neiGe.append({p,dis})

     #def healthRish(self):
        # 回来写 应该用sigmoid

