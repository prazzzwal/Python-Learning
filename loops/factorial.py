
number = int(input("Enter the number to find factorial of: "))

fact = 1

while(number!=0):
    fact = fact*number
    number= number-1

print(fact)