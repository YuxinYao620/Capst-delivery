from request import Request
class Queue():
    # priorityList = []
    def __init__(self):
        self.queue = []
        self.index = 0
        # self.queue.append(request)

    def addRequest(self,request):
        self.queue.append(request)
        self.index += 1
        if self.index > 1:
            self.__insert(self.index-1)

    def __parent(self,index):
        return index//2

    def __leftChild(self,index):
        return 2*index+1

    def __rightChild(self,index):
        return 2*index+2

    def __insert(self, i):  # create smallest node
        if self.index <= 0:
            return
        parent = self.__parent(i)
        if self.queue[i].remainingTime() < self.queue[parent].remainingTime():
            self.queue[i], self.queue[parent] = self.queue[parent], self.queue[i]
            i = parent
            self.__insert(i)

        else:
            return

    def __heapify(self,i):
        l = self.__leftChild(i)
        r = self.__rightChild(i)
        min = i
        if l < self.index and self.queue[i].remainingTime() > self.queue[l].remainingTime() :
            i = l
        if  r < self.index and self.queue[i].remainingTime() > self.queue[r].remainingTime():
            i = r

        if i != min:
            self.queue[i] , self.queue[min] = self.queue[min] , self.queue[i]
            self.__heapify(i)

    def defleast(self,request):
        i = self.queue.index(request)
        self.queue[i], self.queue[-1] = self.queue[-1],self.queue[i]
        self.queue.pop()
        self.index -= 1
        self.__heapify(i)

    def __str__(self):
        return str(self.queue)





