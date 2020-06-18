from priorityqueue import Queue
from request import Request
# from .Shop import Shop
from pharm import Pharm
from user import User
from item import Item
import time
from gero import Gerocery
from volunteer import Volunteer
it = Item("a",True)
itx = Item("b",True)
s1 = Pharm("p1",(2,2),[it,3])
s2 = Pharm("p2",(4,4),[it,2])

u1 = User("A",10,"add1",(5,5),["a"])
u2 = User("B",10,"add2",(3,3),["a"])
# v1 = Volunteer("info1",(1,1),True)

s2.updateStock(itx,2)

r1 = Request(u1)
r1.addItem(it,1)
r2 = Request(u2)
r2.addItem(it,1)
# r2.addItem(itx,1)
# r3 = Request(u2)
# r3.addItem(itx,1)
# time.sleep(2)
r4 = Request(u1)
r4.addItem(it,2)

# r5 = Request(u1)
it.requestqueue.runRankCost()
# for i in r1.medicine:
#     i.keys().addRequest()
# r1.medicine[0]
# que = Queue()
# que.addRequest(r1)


# tbc