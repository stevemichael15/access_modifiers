class Person:
    def __init__(self, name, age):
        self.__name = 3 #Private modifier
        self._age = age # Protected modifier
    def show(self):
        print(self.__name)
class Person2(Person):
    def __init(self,name,age):
        super().__init__(name,age)
        print("The second class is called")
    def getdata(self):
        print(self.show())
a=Person2("Michael",45)
a.getdata()