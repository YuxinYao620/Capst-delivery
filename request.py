import time
# from shop import Shop
# from gero import Gerocery
# from pharm import Pharm
# from user import User
from volunteer import Volunteer
from atool import dis
class Request():
     def __init__(self,user,item,amount):
         self.user = user
         self.date = time.localtime()
         # self.emergency = emergency # T or F// marks
         # self.matchInfo = self.match()
         self.medicine = {}
         self.food = []
         self.cost = self.costValue()
         self.matchGero = []
         # self.matchPharm = self.arrangePharm()
         self.matchPharm = []
         # self.totalCost = self.totalCost()
         self.addItem(item,amount)
     def addItem(self,item,amount):
         if item.isMedi():
             self.medicine = {"item":item,"amount":amount}
             self.arrangePharm()
         else:
             self.food.append([item,amount])

         if self.matchPharm != []:
            # self.addRe(item,amount)
            item.requestqueue.addR(self, item, amount)
         else:
            print("request "+ str(self) + "not avaliable in your area.")

     def addRe(self,item,amount):
         item.requestqueue.addR(self, item, amount)

     def startDate(self):
         return self.date

     def nearPharm(self):
         return self.user.neiPh


     def nearGero(self):
         return self.user.nearestGero()

     def remainingTime(self):
         # nowTime= time.localtime()
         # T = nowTime[1:3]
         # S = self.date[1:3]
         timeR = time.mktime(self.date)
         timeT = time.mktime(time.localtime())
         result = (timeT - timeR)//(60*60*24)
         return result

     def costValue(self):
         return self.remainingTime()*100 + self.user.healthRisk

     def arrangeGero(self):
         for i in self.nearGero():
             if i.checkStock(self.food): #check multiple shop for single request and update each time 优先一个商店
                self.matchGero.append(i)

     # def arrangePharm(self):
     #     for i in self.nearPharm():
     #         item = self.medicine[0]
     #         amount = self.medicine[1]
     #         if i[0].checkStock(item):
     #             self.matchPharm.append({"shop":i[0],"dis":i[1]})
     #     return self.matchPharm

     def arrangePharm(self):
         for i in self.nearPharm():
             # item = self.medicine[0]
             item = self.medicine.get("item")
             # amount = self.medicine[1]
             # amount = self.medicine.get("amount")
             if i[0].checkStock(item):
                 self.matchPharm.append(i)
         return self.matchPharm

     def getDis(self,shop):
         for i in self.matchPharm:
             if shop == i[0]:
                 return i[1]

     def totalCost(self,shop):
         return self.cost + self.getDis(shop)
     # def matchPh(self,listOfPharm):
     #     self.matchPharm.append(listOfPharm)
     def __str__(self):
         return str(self.user )+ str(self.medicine)
     
     # def arrangeVolunteerP(self):
     #     minDis = 2
     #     for i in self.nearPharm():
     #         if i.availablity:
     #             s = i.dis(self.user)
     #             if s<minDis:
     #                 minDis = s
     #                 global result
     #                 result = i
     #     return result





