class Student:

    ## parameterized constructor
    def __init__(self,name,faculty):
        self.name = name
        self.faculty = faculty

    def intro(self):
        print(f"I am {self.name} and I study under the faculty {self.faculty}")

class Teacher:
    ##default constructor
    def __init__(self):
        self.name = "Unknown"
        self.faculty = "Not Assigned"

    def intro(self):
        print(f"I am professor {self.name} and i teach students of faculty {self.faculty}")    

class College:

    #constructor supporting defaault and parametrrized behvior
    def __init__(self,uni_name = "Tribhuwan University"):
        self.name = uni_name

    def info(self):
        print(f"This college is affiliated to {self.name} ")    


#Student objects
s1 = Student("Prajwal","CSIT")
s1.intro()

#Teacher objects
t1 = Teacher()
t1.intro()

#College objects
c1 = College("Pokhara University")
c1.info()

c2 = College()
c2.info()