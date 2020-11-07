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