x = int(input("Enter ny number to check if it is divisible by 5 or 11: "))

if(x%5==0 and x%11==0):
    print("Number is divisible by both 5 and 11")
elif(x%5==0 and x%11 != 0):
    print("Number is divisible by 5 only")
elif(x%5!=0 and x%11 ==0):
    print("Number is divisible by 11 only")
else:
    print("Number can't be divided by 5 or 11")