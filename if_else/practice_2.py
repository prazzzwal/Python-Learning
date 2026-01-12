from datetime import date
import time

name = input("Enter your name:")
today = date.today()


#escape sequence
print(f"""\n Dear {name},\n You are selected \n {today}""")

t = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))

if(hour > 0 and hour<12):
    print("Good Morning sir")
elif(hour>=12 and hour<=17):
    print("Good Afternoon sir")
elif(hour>17 and hour<=0):
    print("Good Evening sir")
