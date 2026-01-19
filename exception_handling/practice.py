num = int(input("Enter number to find multiplication of: "))

try:
    for i in range(1,11):
        print(f"{num} X {i} = {num * i}")
except ValueError:
    print("Invalid Input")