import atool
class requestQ():
    def __init__(self,item):
        self.item = item
        self.requestamount = 0
        self.shopamount = 0
        # self.waitList = [] #?? wait to be sent?
        # self.addList = []
        self.shopList = []
        self.userCount = 0
        self.userList = []
        self.edge = []
        self.graph = []
        self.matchedResult = []

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
            # graph[indx+1][indshop+1+self.userCount] += amount

            userIndex = self.userCount + 1
            tempUserList.append(request.user)
        else:
            userIndex = self.userList.index(request.user)

        # if request.matchPharm == []:
        #     raise TypeError
        for shop,dis in request.matchPharm:
            # shop = index.get("shop")
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
        # for index,value in enumerate(self.edge):
        #     # graph[0][value[1]] = value[0].medicine[1]
        #
        #     for j in value[2]:
        #         graph[index+1][1+self.userCount+j] = 100
        #         graph[self.userCount+j+1][edgeLength-1] = {"flow":self.shopList[j].getStock(),"distance":value[0].getDis(self.shopList[j])}#get the shop distance user
        #
        for i in self.edge:
            graph[0][i[1]] = i[0].medicine[1]
            for j in i[2]:
                # shop = self.shopList[j]
                graph[i[1]][1+self.userCount+j] = 100+i[0].matchPharm[j][1]

        for s in range(len(self.shopList)):
            shop = self.shopList[s]
            graph[1 + self.userCount + s][edgeLength - 1] = shop.getStock()
            # print(shop.getStock())

        print(graph)

        self.FFAMatch(graph,edgeLength)

    def FFAMatch(self,graph,edgelength):
        source = 0
        sink = edgelength-1
        parent = [-1] * (edgelength)
        max_flow = 0

        while self.BFS(source, sink, parent,edgelength,graph):

            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, graph[parent[s]][s])
                s = parent[s]

            # Adding the path flows
            max_flow += path_flow

            # Updating the residual values of edges
            v = sink
            while (v != source):
                u = parent[v]
                graph[u][v] = graph[u][v] - path_flow
                graph[v][u] = graph[v][u] + path_flow
                v = parent[v]
        print(graph)
        return max_flow

    def BFS(self,s,t,parent,edgeLength,graph):
        visited = [False] * (edgeLength)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            u = queue.pop(0)
            # if u>0 and u < self.userCount+1:
            for ind, val in list(sorted(enumerate(graph[u]),key = lambda x:x[1])):
                # if len(val) == 2:
                #     val = val[1]
                if visited[ind] == False and val > 0:#index 链接之后的点
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
            #
            #     for ind, val in sorted(enumerate(graph[u]),key = lambda x: self.userList[ind].getDis(self.shopList[shop]) if ind<self.userCount+1 and ind>0 else ):
            #         if visited[ind] == False and val > 0:#index 链接之后的点
            #             queue.append(ind)
            #             visited[ind] = True
            #             parent[ind] = u
            # else:
            #     for ind, val in enumerate(graph[u]):
            #         if visited[ind] == False and val > 0:#index 链接之后的点
            #             queue.append(ind)
            #             visited[ind] = True
            #             parent[ind] = u

            # tempList = []
            # for ind,val in enumerate(graph[u]):
            #     tempList.append([ind,val])




        return True if visited[t] else False




    # if ind > self.userCount and ind < (edgeLength - 1):

    # def compare(self,list):
    #     tempList = []
    #     for i in list:
    #         if len(i)>1:
    #             tempList.append(i)
    #     sorted(tempList,key = lambda x: x[1][1])
    #     for i in
    #

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


