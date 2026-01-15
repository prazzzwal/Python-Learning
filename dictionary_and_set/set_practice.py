#creating a set
my_set = {"Prajwal","Hello",True,1,0,False,6.9}
print(my_set) #set treat 1 and True as same and avoid duplication,same goes for 0 and False


#accessing set elements
thisset = {"apple", "banana", "cherry"}

if "banana" in thisset:
    print("Banana present")

if "pear" not in thisset:
    print("Pear isnt present in the set")

#empty set
empty_set = {} #using {} creates a dictionary
print(type(empty_set))

empty_set = set() #we cant use {} because it creates a dictionary
print(type(empty_set))

#frozen set
lst = ["hello","hi",5,3.6,True,1]
frozen_lst = frozenset(lst) #converting list to frozen set
print(frozen_lst)