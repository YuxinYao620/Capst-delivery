###### Introduction:
   During the pandemic, lots of people with diseases like asthma are facing high risks when they buy necessaries and medicines
outside. The system is built up to serve as
many vulnerable people as possible with
prescription medicine and food from their
neighbouring groceries and pharmacies.

###### Problem defination
The main problem of the system is to satisfy
the requests made by users with least cost as
far as possible, so this problem is an optimal
problem, which is trying to maximize the
potential to satisfy users' requests. To solve this
optimization problem and increase the
efficiency of the delivery process, some
algorithms are applied. 

###### Features:
   * Used Ford-Fulkerson algorithm algorithm to find the best solution for matching shops and user
   in order to make sure maximum amounts of items that could be
delivered to users.
   * The result of matching will be passed to each shop together with the information 
   of requests and users. 
   * Used heap to decide the priority of sending packages accroding to the health risk 
   and distance of the users.
   
###### Example:
   An example is shown in the main.py, where 2 shops, 3 users and 2 items are initialized.
   The result of the matching and the order of delivering is shown for different shops.
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
it1.requestqueue.runRankCost()
it2.requestqueue.runRankCost()
s1.priQ.show()
s2.priQ.show()
