

a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))

sum = a+b
remainder = a%b

variable_check = input("Enter varaible to be checked:")

print(f"The sum is {sum}")
print (f"The remainder is {remainder}")

variable_type = type(variable_check)

print(f"The variable is of type {variable_type}")


ip = int(input("Enter number to be squared:"))
square = ip**2

print(f"The square of {ip} is {square}")