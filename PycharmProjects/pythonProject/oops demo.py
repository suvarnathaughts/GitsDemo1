# classes are user defined blueprint or prototype
#for e.g. calculator is one of the class in this we have multiplication, addition, substraction#methods, class variables, instance variables, constructor etc.

#so any one can use this blueprint to generate a calculator


class calcu:    # this is the syntax of class
    num = 100   # class variable

    def getdata(self):   # method in class is same as function
        print("i am now executing methods in class")

obj =calcu() # syntax to create object in python and we use object to call class
obj.getdata()    # we use object to call method
obj.num          # we use object to call variable
print(obj.num)