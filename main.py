from pharm import Pharm
from user import User
from item import Item

it1 = Item("a",True)
it2 = Item("b",True)
s1 = Pharm("p1",(2,2),[it1,3])
s2 = Pharm("p2",(4,4),[it1,2])
u1 = User("A",10,"address1",(5,5),["a"])
u2 = User("B",10,"address2",(1,1),["a"])
u3 = User("C",10,"address3",(0,-1),["a"])

s2.updateStock(it2,2)
u1.sendRequest(it1,1)
u2.sendRequest(it1,2)
u3.sendRequest(it1,1)
it1.requestqueue.runRankCost()
it2.requestqueue.runRankCost()
s1.priQ.show()
s2.priQ.show()
