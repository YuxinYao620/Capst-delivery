class node():
    def __init__(self,parent,next,flowOfatob):
        self.parent = parent
        self.next = next
        self.flow = flowOfatob

    def flowchange(self,num):
        self.flow = self.flow + num

    def flow