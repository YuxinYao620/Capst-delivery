# from request import Request
class Queue():#priorityQueue
    # priorityList = []
    def __init__(self,shop):
        self.queue = []
        self.index = 0
        self.shop = shop
        # self.queue.append(request)

    def addRequest(self,request,amount):
        # self.queue.append({"request":request,"amount":amount})
        self.queue.append([request,amount])
        self.index += 1
        if self.index > 1:
            self.__insert(self.index-1)

    def __parent(self,index):
        return index//2

    def __leftChild(self,index):
        return 2*index+1

    def __rightChild(self,index):
        return 2*index+2

    def __insert(self, i):  # create smallest node #index = i
        if self.index <= 0:
            return
        parent = self.__parent(i)
        # a = self.queue[i][0]
        if self.queue[i][0].totalCost(self.shop) < self.queue[parent][0].totalCost(self.shop):
            self.queue[i], self.queue[parent] = self.queue[parent], self.queue[i]
            i = parent
            self.__insert(i)

        else:
            return

    def __heapify(self,i):
        l = self.__leftChild(i)
        r = self.__rightChild(i)
        min = i
        if l < self.index and self.queue[i][0].totalCost(self.shop) > self.queue[l][0].totalCost(self.shop):
            i = l
        if  r < self.index and self.queue[i][0].totalCost(self.shop)> self.queue[r][0].totalCost(self.shop):
            i = r

        if i != min:
            self.queue[i] , self.queue[min] = self.queue[min] , self.queue[i]
            self.__heapify(i)

    def defleast(self,request):
        i = self.queue.index(request)
        self.queue[i], self.queue[-1] = self.queue[-1], self.queue[i]
        self.queue.pop()
        self.index -= 1
        self.__heapify(i)

    def __str__(self):
        return str(self.queue)

    def showqueue(self):
        for i in self.queue:
            print(str(self.shop)+ ' : ' + str(i[0].user) +" requested "+ str(i[0].medicine) +' address: '+str(i[0].user.address)+ ' at position: '+str(i[0].user.position) )


    def show(self):
        # print(self.queue)
        self.showqueue()


        # print(self.shop +' : '+ str())

    def send(self):
        #everytime send every request, every 1 hour send once
        #when send, update all stock in the shop.
        #refresh the priorityqueue
        pass
    #
    # def match(self):
    #     #find shop and user mentioned
    #     #
    #
    #     pass
