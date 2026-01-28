
#creating a class
class Person:
    name = "Prajwal"
    occupation = "student"
    ambition = "Data Scientist"

    def info(self):
        print(f"Hello.its me {self.name} and I am to be a {self.ambition}")

#creating object
a = Person()

#accessing class method with created object
a.info()