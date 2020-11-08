Input: user: User, disease&risk: hashTable(K:disease, V:value)
for all disease in User's disease list:
    let risk := value of disease in disease&risk or 0
    User.cost := User.cost - risk

Input request:Request
    costValue := request.elaspedTime + the cost of user made the request

Input r:Request q:reqestQueue
if demand + amount > supply + all stock request's matched shop
    then reject reqeust
    end this program
else:
    initialize userIndex := 0
    initialize shopIndex := empty array
    if user is not in the reqeustQueue.userList:
        then add the user in reqeustQueue.userList
        userIndex := theindex of this user in userList
            for shop in match shop list of the request
                if the shop exist in the request queue:
                    then shopIndex append the index of the shop in the queue
                else
                    add the shop into the queue
                    shopIndex append the index of the shop in the queue
                    add the stock of the shop to the supply of the queue
    if the user already inside the edge list
        then add the amount of the item to the request with lower cost in the edge list
        delete the higher cost request
    else
        edge append array of [r,userIndex,shopIndexList]

BFS
Input: parent, edgeLength,graph
    initialize visited as an array with length at edgeLength,filled with False
    initialize queue as an array contains 0
    vistied[0] := True
    while the queue is not empty:
    do pop the first element of the queue.
        for every set (index, value) as a set of the sorted enumerate u th row of the graph according to it's capacity of the edge
            if the vistied[index] == False and value >0
                append the index to the queue
                vistied[index] := True
                parent[index] := True
    endWhile
    if the vistied[-1] == True, return Ture, otherwise False

Input List:edge
initialize graph := a zero matrix of edgeLength by edgeLength
let userNum := total number of user in the queue
for i in edge list:
    let iIndex = userIndex of i
    graph[0][iIndex] = the request amount of user from i
    #first row is from start node to every users
    for j in match Shop List # the shopIndex can lead to corresponding shop object
        graph[iIndex][1+userNum+ j] := 100 + the distance from the user to the match shop
    #second to the number of user th row record the connection between user to shops. The index shows their position in matrix
    #100 is the max request amount, prevent the situation that the shop has enough stock but can't  provide to user
    #distance is userd to rank
    for shop in range(number of shops in queue)
        shop[1+ userNum + shop][edgelength -1] = stock of each shop


Input r:Request q:reqestQueue
if demand + amount > supply + all stock request's matchShop
    then reject reqeust
    end this program
else:
    initialize userIndex := 0
    initialize shopIndex := empty array
    if user is not in the reqeustQueue.userList:
        then add the user in reqeustQueue.userList
        userIndex := theindex of this user in userList
            for shop in matchShop list of the request
                if the shop exist in the request queue:
                    then shopIndex append the index of the shop in the queue
                else
                    add the shop into the queue
                    shopIndex append the index of the shop in the queue
                    add the stock of the shop to the supply of the queue
    if the user already inside the edge list
        then add the amount of the item to the request with lower cost in the edge list
        delete the higher cost request
    else
        edge append array of [r, userIndex, shopIndexList]



struct requestQueue{
    Int : demand # total amount requested of request in the queue
    Int : supply # sum of stock of shops in the queue
    Array : userList #store all the users in the queue
    Array: shopList #store all the shops in the queue


}

Input task
initialize requestCost :=the cost of the request the task is deliverying for
let distance := the distance between the shop sending the task and the target user
return requestCost + distance*25

Input List:edge
initialize graph := a zero matrix of edgeLength by edgeLength
let userNum := total number of user in the queue
for i in edge list:
    let iIndex = userIndex of i
    graph[0][iIndex] = the request amount of user from i
    #first row is from start node to every users
    for j in matched Shop List
# the shopIndex can lead to corresponding shop object
        graph[iIndex][1+userNum+ j] := 100 + the distance from the user to the match shop
    for shop in range(number of shops in queue)
        shop[1+ userNum + shop][edgelength -1] := stock of each shop


Input task
initialize requestCost :=the cost of the request the task is deliverying for
let distance := the distance between the shop sending the task and the target user
return requestCost + distance*25
