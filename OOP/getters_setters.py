
class Student:

    ## default constructor
    ## gets called automatically is it is default constructor
    def __init__(self):
        self._marks = 50
        print("Default constructor called")
        print(f"The default value is {self._marks}")
        
    #getter
    @property
    def marks(self):
        print(f"Getter called")
        return self._marks
    
    #setter
    @marks.setter
    def marks(self,value):
        print("Setter called")       
        if 0<=value<=100:
            self._marks = value
            print(f"The value is {self._marks}")
        else:
            print("Invalid marks")

s1 = Student() #object creation

print(s1.marks) # getter called

s1.marks = 850 #setter called