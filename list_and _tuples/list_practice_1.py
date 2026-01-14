
print("Enter 5 numbers: ")

numbers = []
sum = 0
for i in range(1,6):
    ip = int(input())
    numbers.append(ip)
    sum+=ip

print(f"The sum is {sum}")
print(numbers)