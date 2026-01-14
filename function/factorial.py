
ip_number = int(input("Enter number to find factorial of: "))

def factorial(x):
    fact = 1
    while x!=0:
        fact = fact*x
        x = x-1
    return fact    

total = factorial(ip_number)
print(f"The factorial of {ip_number} is {total}")


#creating a function that will be used later
def my_function(x):
    pass           