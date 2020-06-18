class Volunteer():
    volunList = []

    def __init__(self,info,position,available):
        self.info = info
        self.position = position
        self.available = available
        Volunteer.volunList.append(self)

    def changeAvailability(self):
        self.available = not self.available

    def exitVolun(self):
        Volunteer.volunList.remove(self)

    def dis(self,position):
        x1 = self.position[0]
        x2 = position[0]
        y1 = self.position[1]
        y2 = position[1]
        return (x1-x2)**2 + (y1-y2)**2
