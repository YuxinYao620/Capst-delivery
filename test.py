class Queue():
    priorityList = []

    def __init__(self):
        self.queue = []
        self.index = 0
        # self.queue.append(request)

    def addRequest(self, request):
        self.queue.append(request)
        self.index += 1
        if self.index > 1:
            self.__insert(self.index-1)
    #
    # def rank(self):
    #     for i in self.queue:
    #
    # # heap

    def __parent(self, index):
        return index // 2

    def __leftChild(self, index):
        return 2 * index + 1

    def __rightChild(self, index):
        return 2 * index + 2

    def __insert(self, i):  # create smallest node
        if self.index <= 0:
            return

        # L = self.__leftChild(i)
        # R = self.__rightChild(i)
        parent = self.__parent(i)
        # if L>self.index :

        if self.queue[i] < self.queue[parent]:
            self.queue[i], self.queue[parent] = self.queue[parent], self.queue[i]
            i = parent
            # if self.queue[i] < self.queue[L] & self.queue[i] <self.queue[R]
            self.__insert(i)
        else:
            return

    def heapify(self,i):
        l = self.__leftChild(i)
        r = self.__rightChild(i)
        min = i
        if l < self.index and self.queue[i] > self.queue[l]:
            i = l
        if  r < self.index and self.queue[i] > self.queue[r]:
            i = r 

        if i != min:
            self.queue[i] , self.queue[min] = self.queue[min] , self.queue[i]
            self.heapify(i)


    def defleast(self,num): #delete a value
        i = self.queue.index(num)
        self.queue[i], self.queue[-1] = self.queue[-1],self.queue[i]
        self.queue.pop()
        self.index -= 1
        self.heapify(i)
        # self.queue = self.queue[0:i-1] + self.queue[i+1:]
        # self.heapify(i)
    def __str__(self):
        return str(self.queue)
s = Queue()
for i in [2,1,9,0,5,3,7]:
    s.addRequest(i)
print(s.queue)
s.defleast(0)
print(s)
s.defleast(5)
print(s)