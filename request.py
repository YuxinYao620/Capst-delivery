import time
from Shop import Shop
from gero import Gerocery
from pharm import Pharm
from user import User
class Request():
     def __init__(self,user,startDate,emergency):
         self.user = user
         self.date = time.localtime()
         self.emergency = emergency # T or F// marks

     def addItem(self,item,amount):
         self.catagoary = self.catagoary.update({item:amount})

     def startDate(self):
         return self.date

     def emergency(self):
         return self.user.vulunable

     def nearPharm(self):
         return self.user.nearestPharm()

     def nearGero(self):
         return self.user.nearestGero()

     def remainingTime(self):
         return time.localtime()-self.date






