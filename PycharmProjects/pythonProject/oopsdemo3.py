class Calci:
    n = 10
    def __init__(self,a, b):
        self.a =a
        self.b =b
        print("i am called automatically when object is created")
    def getdata(self):
        print("i am now method in class")
    def summation(self):
        return self.a + self.b + self.n


object = Calci(2,3)
object.getdata()
print(object.summation())

