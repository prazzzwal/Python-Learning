num = int(input("Enter the number: "))
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i
        if sum > num:
            break
else:
    if sum == num:
        print("The number is a Perfect Number")
    else:
        print("Not a Perfect Number")

