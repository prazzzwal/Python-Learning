
#list uses square bracket with heterogeneous datatypes
#list are mutable i.e values can be changed

list_demo = ['hi','hello',36,56.5]
print(list_demo[1])

list_demo[2]=52

print(list_demo)

##Tuples

fruits = ("apple", "banana", "cherry")

##adding element to tuple

fruit_list = list(fruits) #converting tuple to list
fruit_list.append("guava","pineapple")

fruits = tuple(fruit_list) #converting list back to tuple 

#unpacking tuples
(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)