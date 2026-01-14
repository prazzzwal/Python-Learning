numbers = []
size = int(input("Enter the size of list: "))

#taking input from user
for i in range(0,size):
    ip = int(input())
    numbers.append(ip)

for i in range(0,size):
    for j in range(0,size-i-1):
        if(numbers[j]>numbers[j+1]):
            numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
        
            
second_largest = numbers[-2]
print(f"The second largest number is {second_largest}")
