import calculator as calculator




class ChildimpI(calcu):
    num2 = 200
    def __init__(self):
        calculator.__init__(self, 2, 10)


    def getcompletedata(self):
        return self.num2 + self.num + self.summation()


obj= ChildimpI()
print(obj.getcompletedata())