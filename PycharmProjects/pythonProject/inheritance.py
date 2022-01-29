from oopsdemo3 import Calci


class child(Calci):
    n2 = 10

    def __init__(self):
        Calci.__init__(self,2, 3)
    def getcompletedata(self):
        return self.n2+self.n+self.summation()



obj3 = child()
print(obj3.getcompletedata())
