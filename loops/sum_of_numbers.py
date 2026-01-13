print("Enter numbers to find the sum (enter 0 to stop):")

total = 0

while True:
    num = int(input())
    if num == 0:
        break
    total += num

print(f"The sum is {total}")
