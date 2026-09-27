class mobile:
    def __init__(self,cost,modle_name,colour):
        self.cost=cost
        self.modle_name=modle_name
        self.colour=colour
    def data(self):
     print("cost of mobile is ",self.cost)
     print("modle number of mobile is ",self.modle_name)
     print("colour of mobile is ",self.colour)
x=mobile(100000,"i5","white")
x.data()
