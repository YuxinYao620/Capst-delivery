from pharm import Pharm
from user import User
from item import Item
# item('name of item', boolean indicating whether the item is a medicine)
it1 = Item("a",True)
it2 = Item("b",True)
# Pharm('name of pharmacy',latitude and longitude of the pharmacy,the stock of items)
s1 = Pharm("p1",(2,2),[it1,3])
s2 = Pharm("p2",(4,4),[it1,2])
# user('name of user',age of user,address of user, latitude and longitude of user, the disease of user has)
u1 = User("A",10,"address1",(5,5),["a"])
u2 = User("B",10,"address2",(1,1),["a"])
u3 = User("C",10,"address3",(0,-1),["a"])
# add new item to shops
s2.updateStock(it2,2)
# add request for users
u1.sendRequest(it1,1)
u2.sendRequest(it1,2)
u3.sendRequest(it1,1)
u2.sendRequest(it2,1)
it1.requestqueue.runRankCost()
it2.requestqueue.runRankCost()
s1.priQ.show()
s2.priQ.show()
