import atool
class requestQ():
    def __init__(self,item):
        self.item = item
        self.requestamount = 0
        self.shopamount = 0
        self.waitList = [] #?? wait to be sent?
        # self.addList = []
        self.shopList = []
        self.userCount = 0
        self.userList = []
        self.edge = []

    def addR(self,request,item,amount):
        tempUserList = []
        tempAmount = self.requestamount + amount
        tempshop = self.shopamount
        tempshopList = []
        shopIndexList = []
        tempShopAmount = 0
        userIndex = 0
        # if request.user not in self.userList:
        if not atool.In(request.user,self.userList):
            # indx = self.userList.index(request.user)
            # indshop = self.shopList.index(shop)
            # self.edge +=
            # self.graph[indx+1][indshop+1+self.userCount] += amount

            userIndex = self.userCount + 1
            tempUserList.append(request.user)
        else:
            userIndex = self.userList.index(request.user)

        # if request.matchPharm == []:
        #     raise TypeError
        for shop,dis in request.matchPharm:
            if shop not in self.shopList:
                tempShopAmount += 1
                tempshop += shop.checkStock(item)
                tempshopList.append(shop)
                shopIndexList.append(len(self.shopList)+tempShopAmount-1)
            else:
                shopIndexList.append(self.shopList.index(shop))

        if tempAmount > tempshop:
            print("rejected :"+str(request))
            print(tempAmount)
            print(tempshop)
            # self.shopList.pop(-1)
            pass

        else:
            self.shopList = self.shopList + tempshopList
            # self. userList = self.userList.append()
            self.requestamount += tempAmount
            self.shopamount += tempshop
            self.userCount = self.userCount +len(tempUserList)
            # addList = [request,userIndex, shopIndexList]
            self.createEdge(request,userIndex,shopIndexList)
            # self.edge.append([request,userIndex, shopIndexList])  # userCount mean the index of user,request give the flow
            print(str(self.item.name)+str(self.edge) + str(self.edge[0][0].medicine[1]))
            # self.addList.append([request, item, amount])
        #build edges
    #every 5min run once or every 50 inputs
    def runRankCost(self):
        graph = []
        edgeLength = len(self.shopList)+self.userCount+2
        for i in range(edgeLength):
            row = []
            for j in range(edgeLength):
                row.append(0)
            graph.append(row)
        # print(graph)
        #write edges i
        # nto graph
        for index,value in enumerate(self.edge):
            graph[0][value[1]] = value[0].medicine[1]

            for j in value[2]:
                graph[index+1][1+self.userCount+j] = 100
                graph[self.userCount+j+1][edgeLength-1] = self.shopList[j].getStock()
                #result
                # for j in value[2]:
                #     graph[index][edgeLength-1] = self.shopList[j].stock[1]

        print(graph)




        print(graph)


    def createEdge(self,request,userIndex, shopIndexList):  #[request,userIndex, shopIndexList]  = list
        if self.edge == []:
            self.edge = [[request,userIndex,shopIndexList]]
        else:
            for i in self.edge: #check same user
                if i[0].user == request.user:
                    if i[0].cost>=request.cost:
                        i[0].medicine[1] += request.medicine[1]

                    else:
                        i[0].cost = request.cost
                    self.userCount = self.userCount - 1
                    return

            self.edge.append([request,userIndex,shopIndexList])
            return
