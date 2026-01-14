def factorial(x):
    """funcion calculates the factorial of the input number"""
    if(x==1 or x==0):
        return 1
    else:
        return x * factorial(x-1)
    

ip = int(input("Enter number to find factorial of: "))

op = factorial(ip)
print(f"The factorial of {ip} is {op}")