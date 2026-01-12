
principal = float(input("Enter the initial amount/principal: "))
rate = float(input("Enter the rate: "))
time = float(input("Enter time in years:"))

interest = (principal*rate*time)/100
print(f"The interest for Rs {principal} in {time} years at rate of {rate}% is Rs {interest}")