
class Employee:

    def __init__(self,id=420,name="Prajwal"):
        self.id = id
        self.name = name

    def details(self):
        print(f"Employee id :{self.id}\nEmployee name :{self.name}")

##multilevel inheritance
class Programmer(Employee):
    def __init(self,language="Python"):
        self.language = language


    def info(self):
         print(f"The default language is {self.language}")


e1 = Employee()
p1 = Programmer("lawjarp",69)

e1.details()

p1.details()