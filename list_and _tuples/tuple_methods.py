tuple1 = (5,7,45,485,87,7,5,4,1,46,6,64,7)

# count method

occurence = tuple1.count(7) # counts the occurence of the element
print(f"The number 7 occurs {occurence} times")


#index() method

index = tuple1.index(7) # returns the first occurence of the element present in tuple
print(f"Element 7 occurs first at index {index}")

#len() method
length = len(tuple1)
print(f"The length of tuple is {length}")