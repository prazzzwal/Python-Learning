# OOP/
# ├── 01_class_and_object.py
# ├── 02_init_and_instance_variables.py
# ├── 03_class_variables.py
# ├── 04_instance_methods.py
# ├── 05_static_methods.py
# ├── 06_class_methods.py
# ├── 07_encapsulation.py
# ├── 08_inheritance.py
# ├── 09_method_overriding.py
# ├── 10_polymorphism.py
# ├── 11_abstraction.py
# ├── 12_interfaces_like_behavior.py
# ├── 13_magic_dunder_methods.py
# ├── 14_composition_vs_inheritance.py
# ├── 15_real_world_example.py


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