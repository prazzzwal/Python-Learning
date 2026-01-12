a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if(a == b):
    print("Both numbers are same")
elif(a<b):
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")