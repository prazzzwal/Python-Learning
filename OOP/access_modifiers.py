class Parent:
    
    #attributes
    publicData = "Public Data" #public
    _protectedData = "Protected Data" #protected
    __privateData = "Private Data" #private

    #method
    def accessPrivate(self):
        print(f"{self.__privateData} accesed inside class")


class Child(Parent):

    def accessProtected(self):
        print(f"{self._protectedData} accessed from child class")


c1 = Child()
c2 = Child()

c1.accessProtected()

print(f"{c1.publicData} accessed  by child class object")

# print(c2.__privateData) cant access as it is private method in the parent class
